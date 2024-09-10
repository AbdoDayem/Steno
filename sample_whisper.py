import whisper

model = whisper.load_model("base")
result = model.transcribe("sample_audio/rockdj.mp3")
print(result["text"])
