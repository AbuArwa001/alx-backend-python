# syntax=docker/dockerfile:1
FROM ubuntu:22.04
# Install dependencies
RUN apt-get update && \
    apt-get install -y python:3.10 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Create a virtual environment
RUN python3 -m venv /venv
# Set the virtual environment as the default Python environment
ENV PATH="/venv/bin:$PATH"
# Install the application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code
COPY . /messaging_app
WORKDIR /messaging_app
# Expose the port the app runs on
EXPOSE 8000
# Set the entrypoint to run the application\
ENTRYPOINT ["python", "manage.py"]
# Set the environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=messaging_app.settings
# Build the Docker image using the docker build command
docker build -t messaging_app .
# Run the Docker container using the docker run command
docker run -p 8000:8000 messaging_app
# Note: Make sure to have a requirements.txt file in the same directory as this Dockerfile
# that contains the necessary Python packages for your application.
# You can add any other dependencies your application requires.
# To run the application, you can use the following command:
# docker run -p 8000:8000 messaging_app
# This will map port 8000 of the container to port 8000 on your host machine.
# You can then access the application at http://localhost:8000
# Make sure to adjust the port if your application runs on a different port.
# If you need to run database migrations, you can do so by running:
docker run -it messaging_app python manage.py migrate
# This will apply any pending migrations to your database.      