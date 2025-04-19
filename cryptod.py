import requests 
import pandas as pd

def fetch_data(symbol='BTCUSDT', interval='1h', limit=100):
    url = f"https://api.binance.com/api/v3/klines"
    
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        "Open Time", "Open", "High", "Low", "Close", "Volume",
        "Close Time", "Quote Asset Volume", "Number of Trades",
        "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"
    ])

    df = df[["Open Time", "Open", "High", "Low", "Close", "Volume"]]
    df["Open Time"] = pd.to_datetime(df["Open Time"], unit='ms')
    df[["Open", "High", "Low", "Close", "Volume"]] = df[["Open", "High", "Low", "Close", "Volume"]].astype(float)

    return df

if __name__ == "__main__":
    df = fetch_data()  # ← We call the function properly here
    print(df.head())      