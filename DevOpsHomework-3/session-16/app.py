"""Session 16 CI/CD demo application."""

from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@app.route("/")
def home():
    return "<h1>Hello from CI/CD</h1><p>Session 16 demo</p>"


@app.route("/health")
def health():
    return jsonify({"status": "ok", "sum": add(2, 3)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
