from flask import Flask, request, jsonify
from flask_cors import CORS
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
    data = request.get_json()
    url = request.headers.get('Origin')
    print(data)
    print(url)

    if request.method=='POST':
        URL = request.data.decode("UTF-8")
        print(request.data)
        # return 200, 'URL posted to backend'

        data = request.get_json()
        url = request.headers.get('Origin')
        print(data)
        print(url)
        return 200, url
    else:
        return 200, URL

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
