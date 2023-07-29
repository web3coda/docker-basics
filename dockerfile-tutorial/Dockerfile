# Use official Python base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt (contains the Python dependencies) into the image at /app
COPY requirements.txt /app/

# Install the Python dependencies from requirements.txt, --no-cache-dir tells pip not to use/store any cache
# requrements.txt only contains Flask as this is a simple app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the image at /app
COPY . /app

# Expose port 8000 for the Flask app
EXPOSE 8000

# Define the command to run the Flask app
CMD ["python", "app.py"]