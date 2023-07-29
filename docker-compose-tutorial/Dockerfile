# Taking Python 3.7 installed on Alpine Linux as base image
FROM python:3.7-alpine

# Setting working directory to /app
WORKDIR /app

# Setting environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Installing gcc, musl-dev and linux-headers
RUN apk add --no-cache gcc musl-dev linux-headers

# Copying app.py and requirements.txt to /app
COPY app.py requirements.txt ./

# Install the Python dependencies from requirements.txt, --no-cache-dir tells pip not to use/store any cache
# requrements.txt only contains Flask as this is a simple app
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Flask app
EXPOSE 8000

# Define the command to run the Flask app
CMD ["flask", "run"]