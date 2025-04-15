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