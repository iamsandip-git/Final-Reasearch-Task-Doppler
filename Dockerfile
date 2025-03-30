# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl\
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file first to leverage Docker layer caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the wait-for-db.sh script and make it executable
COPY wait.for.db.sh /app/wait-for-db.sh
RUN chmod +x /app/wait-for-db.sh

# Copy the application code into the container
COPY . /app

# Expose the port that the app runs on
EXPOSE 8000

# Define the entrypoint command
CMD ["sh", "-c", "./wait-for-db.sh && python manage.py runserver 0.0.0.0:8000"]