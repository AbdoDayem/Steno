import whisper
import os
from queue import Queue

PATH = ' '
audios = Queue()

# Sets the path where audio files will be stored.
def set_path(path):
    global PATH
    PATH = path

def transcribe(model, file):
    return model.transcribe(file)['text']

def load_model():
    return whisper.load_model("base")

def next_audio(model):
    global audios
    D = {}
    if not audios.empty():
        print('Decoding')
        audio_path = audios.get()
        print(audio_path)
        D[os.path.basename(audio_path)] = transcribe(model, audio_path)
    return D

def add_audio(audio_file):
    global audios
    audios.put(PATH +'/'+ audio_file)

def setup():
    print('Loading model')
    model = load_model()
    return model