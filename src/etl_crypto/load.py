def save_to_csv(df, filename="crypto_data.csv"):
    if df is not None:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")