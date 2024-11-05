FROM python:3.10.12

# Install Docker CLI
RUN apt-get update && apt-get install -y docker.io

ADD crawl.py .
ADD crawl .
ADD download.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD ./config ./config
CMD ["python", "crawl.py"]
