import requests
from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup

def HtmlAcquisition(url: str):

    #request for HTML
    pageAccess = requests.get(url)
    pageHtml = pageAccess.text
    
    ElasticSearch(url, pageHtml)

def ElasticSearch(url: str, html: str):
    

    esClient = Elasticsearch("https://localhost:9200", ca_certs="certs/ca-cert.pem", basic_auth=("elastic", "Pk507wI0KzaZ"))
    #print(esClient.info())
    esClient.index(index='audiodownload', id=url, document={'content': html})

    esClient.search()


def FileDownload(url: str, fileName: str):
    destination = 'AudioRip/'+ fileName
    print('not yet implemented')

testURL = 'https://en.wikipedia.org/wiki/File:01_-_Vivaldi_Spring_mvt_1_Allegro_-_John_Harrison_violin.ogg'
HtmlAcquisition(testURL)