import requests
from os import listdir
from os.path import isfile, join
import transcribe as t
import time
PATH = 'sample_audio'

def add_audios():
    for f in listdir(PATH):
        if isfile(join(PATH, f)):
            print(f)
            t.add_audio(f)

def send_info(D):
    r = requests.post('http://localhost:5000/transcribe',data=str(D))

def main():
    #wait for audios to be ready
    ready = False
    while not ready:
        time.sleep(1)
        r = requests.get('http://localhost:5000/audio')
        ready = r.content.decode("UTF-8") == 'True'
    #set path and setup
    t.set_path(PATH)
    M = t.setup()
    add_audios()
    more_audios = True
    output_dict = {}
    while more_audios:
        d = t.next_audio(M)
        more_audios = bool(d)
        if more_audios:
            output_dict = output_dict | d
            send_info(output_dict)

if __name__ == "__main__":
    main()
