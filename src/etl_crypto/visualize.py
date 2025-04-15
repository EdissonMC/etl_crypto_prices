import seaborn as sns
import matplotlib.pyplot as plt
from etl_crypto.transform import detect_outliers_iqr
import pandas as pd
from etl_crypto.extract import fetch_crypto_json
from etl_crypto.transform import json_to_dataframe

def plot_outliers(df: pd.DataFrame, column: str):
    """
    Grafica outliers vs datos normales para una columna numérica.
    """
    df = detect_outliers_iqr(df, column)

    plt.figure(figsize=(12, 6))

    # Boxplot
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot de {column}")

    # Scatter con color por tipo
    plt.subplot(1, 2, 2)
    sns.scatterplot(data=df, x=range(len(df)), y=column, hue=f"{column}_outlier", palette={False: "blue", True: "red"})
    plt.title(f"Outliers vs Datos normales: {column}")
    plt.xlabel("Índice")
    plt.ylabel(column)

    plt.tight_layout()
    plt.show()



def visualice_outliers():
    print("Fetching data...")
    data = fetch_crypto_json()

    print("Transforming data...")
    df = json_to_dataframe(data)
    print(df.head())
    plot_outliers(df, "price")
    # plot_outliers(df, "market_cap")
    # plot_outliers(df, "volume_24h")

    # print("Saving data...")
    # save_to_csv(df)


if __name__== "__main__":
    visualice_outliers()