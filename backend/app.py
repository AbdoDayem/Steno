from flask import Flask, request, jsonify
import ast
app = Flask(__name__)
CORS(app)

DATA = "Hello, world"
N = 0
TEXT = {}
URL = ""
@app.route('/', methods=['GET'])
def home():
    global TEXT
    return jsonify(TEXT)

@app.route('/url',methods=['POST','GET'])
def url():
    global URL
    if request.method=='POST':
        URL = request.data.decode("UTF-8")
    else:
        return URL

@app.route('/transcribe', methods=['POST'])
def receive_transcription():
    global TEXT
    global N
    N = N+1
    data = request.data
    print(data)
    dict_str = data.decode("UTF-8")
    TEXT = ast.literal_eval(dict_str)

@app.route('/status', methods=['GET'])
def audios_left():
    global N
    return str(N)

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
