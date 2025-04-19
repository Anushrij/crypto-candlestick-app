import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

def fetchData(symbol='BTCUSDT', interval='1h', limit=100):
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

# Streamlit UI
st.title("📈 Crypto Candlestick Chart")

symbol = st.text_input("Enter Symbol (e.g. BTCUSDT, ETHUSDT)", value="BTCUSDT")
interval = st.selectbox("Select Interval", ["1m", "5m", "15m", "1h", "4h", "1d"])
limit = st.slider("Number of Candles", 50, 500, 100)

if st.button("Fetch Data"):
    df = fetchData(symbol, interval, limit)

    # Plotly Candlestick
    fig = go.Figure(data=[go.Candlestick(
        x=df["Open Time"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )])
    fig.update_layout(title=f"{symbol} - Candlestick Chart", xaxis_title="Time", yaxis_title="Price (USD)")
    st.plotly_chart(fig, use_container_width=True)