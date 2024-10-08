import requests
import json
J = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
D = "{\"blah.mp4\": \"Hello world\", \"giri.mp4\":\"I refuse to do work\"}"
r = requests.get('http://localhost:5000/status')
print(r.content)
r = requests.post('http://localhost:5000/transcribe',data=D)
r = requests.get('http://localhost:5000/status')
print(r.content)
r = requests.get('http://localhost:5000')
print(r.content)