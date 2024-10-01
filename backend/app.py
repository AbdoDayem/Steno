from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return f"Received data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
