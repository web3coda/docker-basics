from flask import Flask
app = Flask(__name__)

# Default route for / path
@app.route('/')
def hello():
    # Return a string
    return "Hello, Docker from Flask app image!"

# Main method
if __name__ == '__main__':
    # Run the app on all available interfaces on port 8000
    app.run(host='0.0.0.0', port=8000)
