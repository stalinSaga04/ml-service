# Use official Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 (Render will map automatically)
EXPOSE 8000

# Start the app with Gunicorn + Uvicorn
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "ml_service:app"]
