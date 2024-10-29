import requests
from elasticsearch import Elasticsearch
import json


def HtmlAcquisition(url: str):

    #request for HTML
    pageAccess = requests.get(url)
    pageHtml = pageAccess.text
    
    ElasticSearch(url, pageHtml)

def ElasticSearch(url: str, html: str):
    
    esClient = Elasticsearch("https://localhost:9200", ca_certs="certs/ca-cert.pem", basic_auth=("elastic", "Pk507wI0KzaZ"))
    esClient.create(index=url, id=url, document={'body': html})
    


def FileDownload():
    print('not yet implemented')

testURL = 'https://en.wikipedia.org/wiki/File:01_-_Vivaldi_Spring_mvt_1_Allegro_-_John_Harrison_violin.ogg'
HtmlAcquisition(testURL)