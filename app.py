from flask import Flask, request, jsonify
from model import predict_scam

app = Flask(__name__)

@app.route("/")
def home():
    return "TrustNet AI Scam Detector Running 🚀"

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    message = data.get("message", "")
    result = predict_scam(message)
    return jsonify({"result": result})

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
