from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    auth = request.headers.get("Authorization", "<none>")
    return f"Hello, World! You passed: {auth[:20]}..."
