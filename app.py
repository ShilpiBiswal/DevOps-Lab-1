from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps Lab 3!"

@app.route("/hello")
def hello():
    return "Hello from feature branch!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
