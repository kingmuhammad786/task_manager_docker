# Use an official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY . /app

# Define the default command to run the app
CMD ["python", "task_manager(latest).py"]
