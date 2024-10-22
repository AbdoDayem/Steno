from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import ast
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DATA = "Hello, world"
N = 10
TEXT = {}
URL = ""
@app.route('/', methods=['GET'])
@cross_origin
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

if __name__ == '__main__':
    app.run(debug=True)
