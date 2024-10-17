import pprint
import whisper
import transcribe
import os

model = transcribe.setup()
pprint.pp(model.transcribe(os.path.abspath('../audio/audiofile.mp3'))['text'])

