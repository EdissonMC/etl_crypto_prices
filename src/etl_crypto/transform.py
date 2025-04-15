import pandas as pd

def json_to_dataframe(data):
    if not data or "data" not in data:
        print("Invalid or empty data received.")
        return None

    crypto_list = data["data"]
    rows = []
    for coin in crypto_list:
        quote = coin["quote"]["USD"]
        rows.append({
            "name": coin["name"],
            "symbol": coin["symbol"],
            "price": quote["price"],
            "market_cap": quote["market_cap"],
            "volume_24h": quote["volume_24h"],
            "percent_change_1h": quote["percent_change_1h"],
            "percent_change_24h": quote["percent_change_24h"],
            "percent_change_7d": quote["percent_change_7d"]
        })

    df = pd.DataFrame(rows)
    return df



def remove_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Elimina outliers de una columna numérica en un DataFrame usando el método IQR.
    Retorna un nuevo DataFrame sin los outliers.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    df_cleaned = df[(df[column] >= lower_limit) & (df[column] <= upper_limit)]
    return df_cleaned


def remove_outliers_iqr_multiple(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Aplica IQR para eliminar outliers de múltiples columnas.
    """
    for col in columns:
        df = remove_outliers_iqr(df, col)
    return df


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Añade una columna booleana que indica si un valor en la columna dada es un outlier.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    df[f"{column}_outlier"] = ~df[column].between(lower_limit, upper_limit)
    return df
