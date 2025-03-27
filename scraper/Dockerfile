FROM python:3.9-slim-bullseye

# Fix repository sources and install dependencies
RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 && \
    apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get install -y --no-install-recommends \
        curl \
        ca-certificates && \
    curl -o /app/wait-for-it.sh \
        https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /app/wait-for-it.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]