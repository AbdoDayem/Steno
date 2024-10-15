import demo_whisper as dw
import asyncio
import requests
from os import listdir
from os.path import isfile, join

PATH = 'sample_audio'

def add_audios():
    for f in listdir(PATH):
        if isfile(join(PATH, f)):
            dw.add_audio(f)

# Run the main function asynchronously and wait for it to finish
async def run_transcription():
    return await dw.main()

async def main():
    #wait for audios to be ready
    ready = False
    while not ready:
        await asyncio.sleep(1)
        r = requests.get('http://localhost:5000/audio')
        ready = r.content.decode("UTF-8") == 'True'
    
    dw.set_path(PATH)
    add_audios()
    task = asyncio.create_task(run_transcription())
    await asyncio.sleep(5)  # Wait for a while before killing
    await dw.kill()  # Call the kill function
    await task  # Wait for the transcription to finish

if __name__ == "__main__":
    asyncio.run(main())
