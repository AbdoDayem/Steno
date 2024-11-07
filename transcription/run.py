import requests
from os import listdir
from os.path import isfile, join
import transcribe as t
import time
PATH = 'app/shared'

def add_audios():
    for f in listdir(PATH):
        if isfile(join(PATH, f)):
            print(f)
            t.add_audio(f)

def send_info(D):
    r = requests.post('http://backend:5001/transcribe',data=str(D))

def main():
    #wait for audios to be ready
    ready = False
    while not ready:
        print('Waiting for audios to be ready', flush=True)
        time.sleep(1)
        r = requests.get('http://backend:5001/audio')
        ready = r.json()
    #set path and setup
    t.set_path(PATH)
    M = t.setup()
    add_audios()
    more_audios = True
    output_dict = {}
    print('Pre- more_audios loop in transcription/run.py', flush=True)
    while more_audios:
        print('Running more_audios loop in transcription/run.py', flush=True)
        d = t.next_audio(M)
        more_audios = bool(d)
        print('more_audios: ', more_audios)
        if more_audios:
            output_dict = output_dict | d
            # send_info(output_dict)
    send_info(output_dict)

if __name__ == "__main__":
    main()
