FROM nikolaik/python-nodejs:python3.9-nodejs18

# System dependencies
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files (using .dockerignore to exclude unnecessary files)
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Run command (modified for Koyeb)
CMD ["python3", "-m", "FallenMusic"]
