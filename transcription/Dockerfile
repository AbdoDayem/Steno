FROM python:3.10.12
# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD run.py .
ADD transcribe.py .

CMD ["python", "run.py"]