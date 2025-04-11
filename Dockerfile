FROM nikolaik/python-nodejs:python3.9-nodejs18

# System dependencies
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create downloads directory
RUN mkdir -p /app/downloads

# Set working directory
WORKDIR /app

# Copy cookies.txt first to leverage Docker cache
COPY cookies.txt ./

# Copy remaining files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Verify cookies.txt exists
RUN if [ -f "cookies.txt" ]; then \
    echo "Cookies file found"; \
    else \
    echo "Warning: cookies.txt not found - YouTube may block requests"; \
    fi

# Run command
CMD ["python3", "-m", "FallenMusic"]
