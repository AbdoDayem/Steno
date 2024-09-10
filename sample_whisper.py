import whisper
import time

start_time = time.time()

model = whisper.load_model("base")
result = model.transcribe("sample_audio/sample_speech.mp3")
print(result["text"])

print("--- %s seconds ---" % (time.time() - start_time))
