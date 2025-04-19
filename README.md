# crypto-candlestick-app

# Crypto Candlestick App

This is a simple app that fetches real-time cryptocurrency candlestick data and displays it in an interactive chart using Plotly and Streamlit.

## Features
- Displays live candlestick charts for selected cryptocurrencies.
- Fetches data from the Binance API.
- Allows users to select different time intervals and crypto pairs.

## Requirements
- Python 3.x
- Libraries: `requests`, `pandas`, `plotly`, `streamlit`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crypto-candlestick-app.git
Create a virtual environment and activate it:
python -m venv venv
.\venv\Scripts\activate   # For Windows
source venv/bin/activate  # For macOS/Linux

Install the required dependencies:

pip install requests pandas plotly streamlit

Run the App
streamlit run app.py
