from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
from flask_cors import CORS
import ast

app = Flask(__name__)
# cors = CORS(app)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

DATA = "Hello, world"
N = 10
TEXT = {}
URL = ""
AUDIO_READY = False

# Extension gets transcription json
@app.route('/', methods=['GET'])
def home():
    global TEXT
    return jsonify(TEXT)

# Communicates the URL
@app.route('/url', methods=['POST', 'GET'])
def url():
    global URL

    if request.method=='POST':
        data = request.get_json()
        URL = data.get('url')
        return jsonify(URL), 200
    else:
        return URL, 200

# Transcription sends python dict of transcription
@app.route('/transcribe', methods=['POST'])
def receive_transcription():
    global TEXT
    global N
    N = N + 1
    data = request.data
    dict_str = data.decode("UTF-8")
    TEXT = ast.literal_eval(dict_str)

# Checks how many audios have been decoded so far
@app.route('/status', methods=['GET'])
# @cross_origin
def audios_transcribed():
    global N
    return jsonify(N), 200

# Let's transcription know when folder has been populated with audio
@app.route('/audio', methods=['GET', 'POST'])
def ready():
    global AUDIO_READY
    if request.method=='POST':
        AUDIO_READY = True
    else:
        return jsonify(AUDIO_READY), 200

if __name__ == '__main__':
    app.run(debug=True)
