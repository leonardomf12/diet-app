# Use an official Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app's code into the container
COPY . .

# Expose the port Dash will run on
EXPOSE 8050

# Define the command to run the app
CMD ["python", "app.py"]
