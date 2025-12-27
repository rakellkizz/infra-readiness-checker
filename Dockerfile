# Base image kept minimal for faster builds and lower attack surface
FROM python:3.11-slim

# Disable Python buffering for real-time logs
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Copy dependency list first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ app/
COPY tests/ tests/
COPY docs/ docs/

# Expose API port
EXPOSE 8000

# Start the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
