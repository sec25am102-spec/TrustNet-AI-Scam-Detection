from flask import Flask, request, jsonify
from model import predict_scam

app = Flask(__name__)

@app.route('/')
def home():
    return "TrustNet AI Scam Detector Running"

@app.route('/detect', methods=['POST'])
def detect():
    text = request.json['message']
    result = predict_scam(text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
