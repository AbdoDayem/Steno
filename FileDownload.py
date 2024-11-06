import requests
from elasticsearch import Elasticsearch
from pprint import pprint
from bs4 import BeautifulSoup

def HtmlAcquisition(url: str):

    #request for HTML
    pageAccess = requests.get(url)
    pageHtml = pageAccess.text
    
    htmlWrite = open("html.txt",'w',encoding=pageAccess.encoding)
    htmlWrite.write(pageHtml)
    htmlWrite.close()

    ElasticSearch(url, pageHtml)

def ElasticSearch(url: str, html: str):
    
    parsedHtml = BeautifulSoup(html, features="html.parser")
    tagDict = dict()
    for tag in parsedHtml.find_all():
        if not tag.name in tagDict.keys():
            tagDict[tag.name] = [tag]
        else:
            tagDict[tag.name].append(tag)

    parsingWrite = open('parsed.txt','w',encoding='utf8')
    pprint(tagDict, stream=parsingWrite)
    parsingWrite.close()
    

    esClient = Elasticsearch("https://localhost:9200", ca_certs="certs/ca-cert.pem", basic_auth=("elastic", "Pk507wI0KzaZ"))
    #print(esClient.info())
    for tag, list in tagDict.items():
        esClient.index(index="audiodownload", id=tag, document=list)

    resp = esClient.search(index = "audiodownload",
        query= {"match": 
                {
                    
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