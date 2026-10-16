from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello from DevSecOps</h1><p>Session 17 pipeline demo</p>"


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/status")
def status():
    return jsonify({"app": "session17-devsecops", "status": "running"})


def greet(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    # Bind all interfaces so the container port mapping works.
    app.run(host="0.0.0.0", port=5001)  # nosec B104
