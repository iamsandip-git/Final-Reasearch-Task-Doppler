# Use an official Python runtime as a parent image
FROM ubuntu:16.04

# Install prerequisites
RUN apt-get update && apt-get install -y \
curl

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
COPY main.py .
# Run migrations and start the scraper script
CMD ["python", "./scraper/main.py"]