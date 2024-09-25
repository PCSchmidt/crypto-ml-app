import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def prepare_data(df, target='price', features=['volume', 'market_cap'], lookback=5):
    for col in [target] + features:
        for i in range(1, lookback + 1):
            df[f'{col}_lag_{i}'] = df[col].shift(i)
    
    df.dropna(inplace=True)
    
    X = df[[f'{feat}_lag_{i}' for feat in features for i in range(1, lookback + 1)]]
    y = df[target]
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    
    return model, scaler

def evaluate_model(model, scaler, X_test, y_test):
    X_test_scaled = scaler.transform(X_test)
    y_pred = model.predict(X_test_scaled)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return mse, r2, y_pred

def plot_predictions(y_test, y_pred):
    plt.figure(figsize=(12, 6))
    plt.plot(y_test.index, y_test.values, label='Actual')
    plt.plot(y_test.index, y_pred, label='Predicted')
    plt.title('Actual vs Predicted Prices')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.legend()
    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def run_ml(df):
    X_train, X_test, y_train, y_test = prepare_data(df)
    model, scaler = train_model(X_train, y_train)
    mse, r2, y_pred = evaluate_model(model, scaler, X_test, y_test)
    plot = plot_predictions(y_test, y_pred)
    
    return {
        'mse': mse,
        'r2': r2,
        'plot': plot
    }

if __name__ == "__main__":
    # For testing purposes
    from etl import run_etl
    df = run_etl()
    results = run_ml(df)
    print(f"MSE: {results['mse']}")
    print(f"R2 Score: {results['r2']}")
