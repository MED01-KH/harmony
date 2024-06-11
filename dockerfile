# Use the official Python image from the Docker Hub
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Install Flask 2.0.2 and Werkzeug 2.0.3
RUN pip install Flask==2.0.2 Werkzeug==2.0.3

# Copy the rest of the application code into the container at /app
COPY . /app/

# Set appropriate permissions for the copied files
RUN chmod -R 777 /app

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
