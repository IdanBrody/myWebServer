# Use a slim Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install Python dependencies
RUN apt-get update && apt-get install -y python3-venv
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONPATH=/app
ENV MYSQL_HOST="mysql-db"

# Install Python dependencies
RUN pip install --no-cache-dir -r Server/requirements.txt

# Expose the port that the Flask app listens on
EXPOSE 5000

# Run the Flask app
CMD ["python", "Server/Main.py"]
