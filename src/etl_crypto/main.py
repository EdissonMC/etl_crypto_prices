from dotenv import load_dotenv

from etl_crypto.extract import fetch_crypto_json
from etl_crypto.transform import json_to_dataframe
from etl_crypto.load import save_to_csv
load_dotenv()  # Esto es obligatorio para que se lea el .env



    
def run_etl():
    print("Fetching data...")
    data = fetch_crypto_json()

    print("Transforming data...")
    df = json_to_dataframe(data)
    print(df.head())
    
    print("Saving data...")
    save_to_csv(df)

if __name__ == "__main__":
    run_etl()