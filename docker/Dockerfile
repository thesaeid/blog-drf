# This Dockerfile is used for local development via docker-compose
FROM python:3.10

# Fix python printing
ENV PYTHONUNBUFFERED 1

# Install all Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project into the container
RUN mkdir /app
WORKDIR /app
COPY ./ /app/
