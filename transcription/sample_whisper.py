import whisper
import os
import asyncio
from queue import Queue

kill_flag = False
PATH = ""
output_dict ={}
q = Queue()
#Tells whisper model to stop running
def kill():
    global kill_flag 
    kill_flag = True

def get_output():
    global output_dict
    return output_dict

#Sets the path where audio files will be stored. Should be a path object
def set_path(path):
    global PATH
    PATH = path

def transcribe(file):
    result = model.transcribe(file)
    return result["text"]   

def load_model():
    return whisper.load_model("base")
        
async def run(model):
    print("test 2")
    D = {}
    global q
    while True:
        await asyncio.sleep(0.5)
        print(q.qsize())        
        if not q.empty():
            print("decoding")
            audio_path = q.get()
            result_text = transcribe(audio_path)
            D[os.path.basename(audio_path)] = result_text
        elif kill_flag:
            break
    print(D)
    return D

#audio_file should be a path object of an audio file inside PATH
def add_audio(audio_file):
    global q
    q.put(os.path.join(PATH,audio_file))
    print(q.qsize())

if __name__ == "__main__":
    print("test")
    model = load_model()
    output_dict = asyncio.run(run(model))