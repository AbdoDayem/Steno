from flask import Flask, request, jsonify
import ast
app = Flask(__name__)

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
        URL = str(request.data)
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
