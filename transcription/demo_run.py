import os
import time
import demo_whisper as dw
import asyncio

dw.set_path("sample_audio")

dw.add_audio("rockdj.mp3")
dw.add_audio("sample_speech.mp3")
dw.add_audio("sample_speech2.mp3")

# Run the main function asynchronously and wait for it to finish
async def run_transcription():
    await dw.main()

async def main():
    task = asyncio.create_task(run_transcription())
    await asyncio.sleep(5)  # Wait for a while before killing
    await dw.kill()  # Call the kill function
    await task  # Wait for the transcription to finish

if __name__ == "__main__":
    asyncio.run(main())
