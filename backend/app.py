from flask import Flask, request, jsonify
import ast
app = Flask(__name__)

DATA = "Hello, world"
N = 0
TEXT = {}
URL = ""
AUDIO_READY = False

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

# Let's transcription know when folder has been populated with audio
@app.route('/audio',methods=['GET','POST'])
def ready():
    global AUDIO_READY
    if request.method=='POST':
        AUDIO_READY = True
    else:
        return str(AUDIO_READY)

if __name__ == '__main__':
    app.run(debug=True)
