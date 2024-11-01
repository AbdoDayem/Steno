import requests
import json
J = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
D = {"blah.mp4": "Hello world", "giri.mp4":"I refuse to do work"}
U = "https://github.com/rtussing/capstone/blob/main/backend/app.py"
r = requests.post('http://0.0.0.0:5001/audio')
'''
r = requests.get('http://0.0.0.0:5001/status')
print(r.content)
r = requests.post('http://0.0.0.0:5001/transcribe',data=str(D))
r = requests.get('http://0.0.0.0:5001/status')
print(r.content)
r = requests.get('http://0.0.0.0:5001')
print(r.content)
r = requests.post('http://0.0.0.0:5001/url',data=U)
r = requests.get('http://0.0.0.0:5001/url')
print(r.content)
r = requests.get('http://0.0.0.0:5001/audio')
print(r.content)'''