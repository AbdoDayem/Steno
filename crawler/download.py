import datetime
import pprint
from elasticsearch import Elasticsearch
import urllib.request
import requests

# Create the client instance
# ELASTIC_PASSWORD = "TCG_7GzN6ZFKej4Fut-m"

# # Create the client instance
# client: Elasticsearch = Elasticsearch(
#     "https://localhost:9200",
#     ca_certs="./certs/ca-cert.pem",
#     basic_auth=("elastic", ELASTIC_PASSWORD)
# )

id = 0

file = open('./html.txt', 'r')
doc_text = file.readlines()
file.close()

matches = [match for match in doc_text if "</audio>" in match]
lines = []
for match in matches:
    lines += match.split()
sources = [line for line in lines if ('src' in line)]

source = sources[0].replace('src=', '').replace('\"', '')

if 'https' not in source: source = 'https:' + source

print(source, flush=True)

urllib.request.urlretrieve(source, f"./app/shared/audiofile.mp3")
id += 1

# Post to backend that the audio is ready
r = requests.post('http://backend:5001/audio')


# doc = {
#     'text': doc_text
# }

# #client.indices.create(index="test-index")

# res = client.index(index="test-index", id=1, document=doc)

# # resp = client.search(
# #     index="test-index",
# #     query={"match": {"text": {"query": "<audio"}}}
    
# # )


# pprint.pp(resp["hits"]["hits"])

# #client.delete(index="test-index", id=1)
# #client.indices.delete(index="test-index")