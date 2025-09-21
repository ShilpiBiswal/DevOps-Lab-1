from flask import Flask
from loguru import logger

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps Lab 3!"

@app.route("/hello")
def hello():
    return "Hello from feature branch!"

@app.before_request
def log_request():
    logger.info("Handling request...")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
