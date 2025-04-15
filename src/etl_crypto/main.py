from dotenv import load_dotenv
import pandas as pd
from etl_crypto.extract import fetch_crypto_json
from etl_crypto.transform import json_to_dataframe,remove_outliers_iqr_multiple
from etl_crypto.load import save_to_csv
load_dotenv()  # Esto es obligatorio para que se lea el .env



def clean_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpieza de outliers sobre columnas relevantes del DataFrame.
    """
    columns_to_clean = ["price", "market_cap", "volume_24h"]
    df_clean = remove_outliers_iqr_multiple(df, columns_to_clean)
    return df_clean


def run_etl():
    print("Fetching data...")
    data = fetch_crypto_json()

    print("Transforming data...")
    df = json_to_dataframe(data)
    print(df.head())

    print("Saving data...")
    save_to_csv(df)


def clean_outliers_on_data():
    print("Fetching data...")
    data = fetch_crypto_json()

    print("Transforming data...")
    df = json_to_dataframe(data)
    print(df.head())

    if df is not None:
        print("Datos obtenidos. Primeras filas:\n", df.head())

        # Limpiar outliers
        df_cleaned = clean_outliers(df)

        # Guardar datos limpios
        df_cleaned.to_csv("crypto_data_cleaned.csv", index=False)
        print("Datos limpios guardados en crypto_data_cleaned.csv")
    else:
        print("No se pudieron obtener datos.")

if __name__ == "__main__":
    # run_etl()
    clean_outliers_on_data()