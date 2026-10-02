# Use python 3.11 base image

from python:3.11-slim

# set working directory

workdir /app

#copy requirements and install dependencies

copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt

#copy rest of the application code

copy . .

#expose the application port

expose 8000

# command to start FastAPI application

cmd ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]