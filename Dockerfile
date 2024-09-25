# Use the official Tiangolo FastAPI image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . /app

# The CMD is already set in the base image, so we don't need to specify it again
# It will use uvicorn to run our app/api.py file
