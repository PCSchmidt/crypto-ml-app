# Crypto ML App

This project is a data engineering and machine learning application that fetches cryptocurrency information, performs ETL (Extract, Transform, Load) operations, conducts Exploratory Data Analysis (EDA), and applies machine learning techniques. The application consists of a FastAPI backend and a Next.js frontend.

## Prerequisites

- Docker
- Node.js (v14 or later)
- npm (v6 or later)

## Backend Setup

The backend is containerized using Docker for easy deployment and consistency across environments.

1. Build the Docker image:
   ```
   docker build -t crypto-ml-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 8000:80 crypto-ml-app
   ```

The backend API will now be accessible at `http://localhost:8000`.

## Frontend Setup

The frontend is built with Next.js and communicates with the backend API.

1. Navigate to the frontend directory:
   ```
   cd nextjs-frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```

The frontend will be accessible at `http://localhost:3000`.

## Usage

1. Start the backend Docker container as described above.
2. Start the frontend development server.
3. Open your browser and navigate to `http://localhost:3000`.
4. The application will fetch cryptocurrency data, perform analysis, and display the results.

## API Endpoints

- `/api/crypto-analysis`: Fetches cryptocurrency data, performs EDA, and returns analysis results.

## Project Structure

- `app/`: Contains the FastAPI backend code
  - `etl.py`: Handles data extraction and transformation
  - `eda.py`: Performs exploratory data analysis
  - `ml_model.py`: Implements machine learning models
  - `api.py`: Defines FastAPI routes
- `nextjs-frontend/`: Contains the Next.js frontend code
  - `pages/`: Next.js pages
  - `components/`: React components
  - `styles/`: CSS styles

## Troubleshooting

- If you encounter issues with the Docker build, ensure you have the latest version of Docker installed.
- For any dependency issues, check that your Node.js and npm versions meet the prerequisites.
- If the frontend fails to fetch data from the backend, verify that both the Docker container and the Next.js development server are running, and that the API endpoint in `nextjs-frontend/pages/api/crypto-analysis.ts` is set to `http://localhost:8000`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).