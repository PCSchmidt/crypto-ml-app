import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface CryptoData {
  eda: {
    price_trend: string;
    volume_trend: string;
    price_volume_correlation: string;
    statistics: {
      price_mean: number;
      price_std: number;
      volume_mean: number;
      volume_std: number;
      price_volume_correlation: number;
    };
  };
  ml: {
    mse: number;
    r2: number;
    plot: string;
  };
}

const CryptoAnalysis: React.FC = () => {
  const [data, setData] = useState<CryptoData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get<CryptoData>('/api/crypto-analysis');
        setData(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch data');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!data) return <div>No data available</div>;

  return (
    <div>
      <h2>Crypto Analysis</h2>
      <div>
        <h3>Price Trend</h3>
        <img src={`data:image/png;base64,${data.eda.price_trend}`} alt="Price Trend" />
      </div>
      <div>
        <h3>Volume Trend</h3>
        <img src={`data:image/png;base64,${data.eda.volume_trend}`} alt="Volume Trend" />
      </div>
      <div>
        <h3>Price vs Volume Correlation</h3>
        <img src={`data:image/png;base64,${data.eda.price_volume_correlation}`} alt="Price vs Volume Correlation" />
      </div>
      <div>
        <h3>Statistics</h3>
        <ul>
          <li>Price Mean: {data.eda.statistics.price_mean.toFixed(2)}</li>
          <li>Price Std Dev: {data.eda.statistics.price_std.toFixed(2)}</li>
          <li>Volume Mean: {data.eda.statistics.volume_mean.toFixed(2)}</li>
          <li>Volume Std Dev: {data.eda.statistics.volume_std.toFixed(2)}</li>
          <li>Price-Volume Correlation: {data.eda.statistics.price_volume_correlation.toFixed(2)}</li>
        </ul>
      </div>
      <div>
        <h3>Machine Learning Results</h3>
        <p>Mean Squared Error: {data.ml.mse.toFixed(4)}</p>
        <p>R2 Score: {data.ml.r2.toFixed(4)}</p>
        <img src={`data:image/png;base64,${data.ml.plot}`} alt="ML Predictions" />
      </div>
    </div>
  );
};

export default CryptoAnalysis;