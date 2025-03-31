# # Use an official Python runtime as the base image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy only the requirements file first to leverage Docker layer caching
# COPY requirements.txt .

# # Install system dependencies and Python packages
# RUN apt-get update && apt-get install -y \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire project into the container
# COPY . .

# # Add the wait-for-it.sh script and make it executable
# # COPY wait-for-it.sh wait-for-it.sh
# # RUN chmod +x wait-for-it.sh

# # Set environment variables
# ENV PYTHONUNBUFFERED=1
# COPY main.py .
# # Default command (can be overridden in docker-compose.yml)
# # CMD ["python", "main.py"]
# CMD python ./scraper/main.py# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Add the wait-for-it.sh script and make it executable
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Ensure main.py is in the correct location
COPY scraper/main.py /app/scraper/main.py

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command (can be overridden in docker-compose.yml)
CMD ["sh", "-c", "/app/wait-for-it.sh db:5432 --timeout=60 --strict -- python /app/scraper/main.py"]