import os
import time
from sample_whisper import kill,get_output,add_audio,set_path
audio_path = "sample_audio"

set_path(audio_path)
audio_file_1 = "rockdj.mp3"
audio_file_2 = "sample_speech.mp3"
add_audio(audio_file_1)
add_audio(audio_file_2)
kill()