# Use an official Python runtime with a specific version
FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# Install system dependencies first
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download wait-for-it.sh directly (no local file needed)
RUN curl -o /app/wait-for-it.sh \
    https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /app/wait-for-it.sh

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire application (excluding .dockerignore patterns)
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="/app"

# Entrypoint command using wait-for-it
CMD ["/app/wait-for-it.sh", "backend:8000", "--", "python", "main.py"]