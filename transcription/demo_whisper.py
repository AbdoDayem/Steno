import whisper
import os
import asyncio
from queue import Queue

kill_flag = False
PATH = ' '
output_dict = {}
q = Queue()

# Tells whisper model to stop running
async def kill():
    global kill_flag 
    kill_flag = True

def get_output():
    global output_dict
    return output_dict

# Sets the path where audio files will be stored.
def set_path(path):
    global PATH
    PATH = path

def transcribe(model, file):
    return model.transcribe(file)['text']

def load_model():
    return whisper.load_model("base")

async def run(model):
    print("Starting transcription")
    D = {}
    global q
    
    while True:
        await asyncio.sleep(0.5)
        print(f'Queue size: {q.qsize()}')
        
        if not q.empty():
            print('Decoding')
            audio_path = q.get()
            D[os.path.basename(audio_path)] = transcribe(model, audio_path)
        
        elif kill_flag:
            print('Stopping transcription.')
            break
    return D

def add_audio(audio_file):
    global q
    q.put(os.path.join(PATH, audio_file))
    print(f'Audio added. Queue size: {q.qsize()}')

async def main():
    print('Loading model')
    model = load_model()
    output_dict = await run(model)
    return output_dict

if __name__ == "__main__":
    asyncio.run(main())
