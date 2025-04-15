
import os
import pandas as pd
import json
from dotenv import load_dotenv
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

load_dotenv()

def fetch_crypto_json():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '100',
        'convert': 'USD'
    }
    # api_key = os.getenv("COINMARKETCAP_API_KEY")
    # print(f"API Key loaded: {api_key}")  # DEBUG: BORRAR LUEGO

    # headers = {
    #     'Accepts': 'application/json',
    #     'X-CMC_PRO_API_KEY': api_key,
    # }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('COINMARKETCAP_API_KEY'),
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        response.raise_for_status()
        data = response.json()
        return data
    # try:
    #     response = session.get(url, params=parameters)
    #     data = json.loads(response.text)
    #     crypto_list = data.get("data", [])

    #     rows = []
    #     for coin in crypto_list:
    #         quote = coin["quote"]["USD"]
    #         rows.append({
    #             "name": coin["name"],
    #             "symbol": coin["symbol"],
    #             "price": quote["price"],
    #             "market_cap": quote["market_cap"],
    #             "volume_24h": quote["volume_24h"],
    #             "percent_change_1h": quote["percent_change_1h"],
    #             "percent_change_24h": quote["percent_change_24h"],
    #             "percent_change_7d": quote["percent_change_7d"]
    #         })

    #     df = pd.DataFrame(rows)
    #     return df

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Connection error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
