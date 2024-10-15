from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

@app.route('/data', methods=['POST'])
def receive_data():
    data = request
    return f"Received data: {data}"

@app.route('/api/v1/transcribe', methods=['POST'])
def startTranscriptions():
    data = request.get_json()
    url = request.headers.get('Origin')
    print(data)
    print(url)
    return jsonify(data), 200

@app.route('/api/v1/transcriptions', methods=['GET'])
def getTranscriptions():
    return 404

@app.route('/api/v1/stop', methods=['GET'])
def stopTranscription():
    return 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)
