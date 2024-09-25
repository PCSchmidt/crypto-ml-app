import requests
import pandas as pd
import os
from datetime import datetime

def fetch_crypto_data(coin='bitcoin', days=30, vs_currency='usd'):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {'vs_currency': vs_currency, 'days': days}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    data = response.json()
    prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    volumes = pd.DataFrame(data['total_volumes'], columns=['timestamp', 'volume'])
    market_caps = pd.DataFrame(data['market_caps'], columns=['timestamp', 'market_cap'])
    
    # Merge all dataframes
    df = prices.merge(volumes, on='timestamp').merge(market_caps, on='timestamp')
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    
    return df

def save_data(df, coin, vs_currency):
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save to CSV
    filename = f"data/{coin}_{vs_currency}_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename)
    print(f"Data saved to {filename}")

def run_etl(coin='bitcoin', days=30, vs_currency='usd'):
    df = fetch_crypto_data(coin, days, vs_currency)
    save_data(df, coin, vs_currency)
    return df

if __name__ == "__main__":
    run_etl()
