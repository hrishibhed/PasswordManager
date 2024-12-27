# FROM python:3.10-slim
# ENV PYTHONDONTWRITEBYTECODE=1 
# ENV PYTHONUNBUFFERED=1         
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --upgrade pip && pip install -r requirements.txt
# COPY . /app/
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate

# EXPOSE 8000
# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1         

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project
COPY . /app/

# Run migrations
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# Run the application
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]