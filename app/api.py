from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import etl, eda, ml_model

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from the Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.9"}

@app.get("/api/crypto-analysis")
async def get_crypto_analysis(coin: str = 'bitcoin', days: int = 30, vs_currency: str = 'usd'):
    # Run ETL
    df = etl.run_etl(coin, days, vs_currency)
    
    # Run EDA
    eda_results = eda.run_eda(df)
    
    # Run ML
    ml_results = ml_model.run_ml(df)
    
    return {
        "eda": eda_results,
        "ml": ml_results
    }
