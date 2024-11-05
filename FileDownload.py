import requests
from elasticsearch import Elasticsearch
from pprint import pprint

def HtmlAcquisition(url: str):

    #request for HTML
    pageAccess = requests.get(url)
    pageHtml = pageAccess.text
    
    htmlWrite = open("html.txt",'w',encoding=pageAccess.encoding)
    htmlWrite.write(pageHtml)
    htmlWrite.close()

    ElasticSearch(url, pageHtml)

def ElasticSearch(url: str, html: str):
    
    
    esClient = Elasticsearch("https://localhost:9200", ca_certs="certs/ca-cert.pem", basic_auth=("elastic", "Pk507wI0KzaZ"))
    print(esClient.info())
    esClient.index(index="audiodownload", id=url, document={"content": html})

    resp = esClient.search(index = "audiodownload",
        query= {"match": 
                {
                    "content": "src"
                }
        }
    )
    elasticWrite = open('search.txt', 'w', encoding='utf8')
    pprint(resp.body, stream=elasticWrite)
    elasticWrite.close()

def FileDownload(url: str, fileName: str):
    destination = 'AudioRip/'+ fileName
    print('not yet implemented')

testURL = 'https://en.wikipedia.org/wiki/File:01_-_Vivaldi_Spring_mvt_1_Allegro_-_John_Harrison_violin.ogg'
HtmlAcquisition(testURL)