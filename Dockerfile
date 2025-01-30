# Use an appropriate base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

<<<<<<< HEAD
# Expose the port the app runs on
EXPOSE 8000

# Command to run your application
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
=======
# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
>>>>>>> ad4e2c1 (ss)
