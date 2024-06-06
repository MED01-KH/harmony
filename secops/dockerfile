# Use the official Python image from the Docker Hub
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Create a SQLite database file
RUN python create_database.py

# Command to run the application
CMD ["python", "app.py"]
