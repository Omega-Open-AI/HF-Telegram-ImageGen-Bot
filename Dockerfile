# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port if needed (adjust if using webhooks)
EXPOSE 8080

# Set environment variables (these can also be passed in at runtime)
ENV TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
ENV HF_API_TOKEN=YOUR_HF_API_TOKEN
ENV REDIS_HOST=redis

# Run the asynchronous Telegram bot
CMD ["python", "main.py"]