import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def plot_price_trend(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['price'])
    plt.title('Price Trend')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    return get_plot_image()

def plot_volume_trend(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['volume'])
    plt.title('Trading Volume Trend')
    plt.xlabel('Time')
    plt.ylabel('Volume')
    return get_plot_image()

def plot_price_volume_correlation(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='price', y='volume', data=df)
    plt.title('Price vs Volume Correlation')
    plt.xlabel('Price (USD)')
    plt.ylabel('Volume')
    return get_plot_image()

def calculate_statistics(df):
    return {
        'price_mean': df['price'].mean(),
        'price_std': df['price'].std(),
        'volume_mean': df['volume'].mean(),
        'volume_std': df['volume'].std(),
        'price_volume_correlation': df['price'].corr(df['volume'])
    }

def get_plot_image():
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def run_eda(df):
    results = {
        'price_trend': plot_price_trend(df),
        'volume_trend': plot_volume_trend(df),
        'price_volume_correlation': plot_price_volume_correlation(df),
        'statistics': calculate_statistics(df)
    }
    return results

if __name__ == "__main__":
    # For testing purposes
    from etl import run_etl
    df = run_etl()
    results = run_eda(df)
    print(results['statistics'])
