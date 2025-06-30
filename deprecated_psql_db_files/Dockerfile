# Use an official Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the requirements and install dependencies
COPY ../requirements.txt main.py /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Dash will run on
EXPOSE 8050

# Define the command to run the app
CMD ["python", "main.py"]
