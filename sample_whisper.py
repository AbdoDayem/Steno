import whisper
import time
import asyncio
from queue import Queue

kill_flag = False

def main():
    result = model.transcribe("sample_audio/sample_speech.mp3")
    print(result["text"])
    
def load_model():
    return whisper.load_model("base")
        
async def run(model, q):
    while True:
        await asyncio.sleep(0.5)        
        if not q.empty():
            print('Hello World')
        if kill_flag:
            break
        
if __name__ == "__main__":
    start_time = time.time()
    q = Queue()
    model = load_model()
    asyncio.run(run(model, q))
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    