# Use the official Python image as a base
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install requests library
RUN pip install requests

# Copy the Django project files into the container
COPY . /app/

# Expose port 8080 to the outside world
EXPOSE 8080

# Define the command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]