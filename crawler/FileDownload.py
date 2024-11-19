import requests
from elasticsearch import Elasticsearch
from pprint import pprint
from bs4 import BeautifulSoup
import urllib

def HtmlAcquisition(url: str):

    #request for HTML
    pageAccess = requests.get(url)
    pageHtml = pageAccess.text
    
    htmlWrite = open("html.txt",'w',encoding=pageAccess.encoding)
    htmlWrite.write(pageHtml)
    htmlWrite.close()

    ElasticSearch(url, pageHtml)

def ElasticSearch(url: str, html: str):
    
    #parsing html into json for elasticsearch
    parsedHtml = BeautifulSoup(html, features="html.parser")
    tagDict = dict()
    for tag in parsedHtml.find_all():
        if not str(tag.name) in tagDict.keys():
            tagDict[str(tag.name)] = [str(tag)]
        else:
            tagDict[str(tag.name)].append(str(tag))
    
    esClient = Elasticsearch("https://localhost:9200", ca_certs="certs/ca-cert.pem", basic_auth=("elastic", "Pk507wI0KzaZ"))
    #print(esClient.info())
    #places each tag in elasticsearch as a separate document
    for tag, tagList in tagDict.items():
        doc = {tag: tagList}
        esClient.index(index="audiodownload", id=tag, document=doc)

    #match for extensions
    resp = esClient.search(index = "audiodownload",
        query= {"match": 
                {
                    "audio": ".ogg"
                }
        }
    )
    #isolates an audio tag containing src
    audioTag = resp.body['hits']['hits'][0]['_source']['audio']
    downloadTag = ''
    for item in audioTag:
        if item.__contains__('src') and downloadTag=='':
            downloadTag = item

    #isolates the src attribute
    tagTokens = downloadTag.split()
    srcAtt = ''
    for token in tagTokens:
        if token.__contains__('src') and srcAtt=='':
            srcAtt = token
    
    #isolate src URL to download
    downloadURL = srcAtt[5:-1]
    if not downloadURL.__contains__('https:'):
        downloadURL= 'https:' + downloadURL
    
    FileDownload2(downloadURL)

    #clear index
    esClient.indices.delete(index='audiodownload')

def FileDownload(url: str):
    lastDotIndex = 0
    print('\n\n'+url)
    for i in range(url.__len__()):
        if url[i]=='.':
            lastDotIndex = i
    extension = url[lastDotIndex:lastDotIndex+4]
    destination = 'media/FileForTranscription'+extension

    response = requests.get(url)
    fileOut = open(destination, 'wb') 
    fileOut.write(response.content)
    fileOut.close()

def FileDownload2(url: str):
    urllib.request.urlretrieve(url, "./app/shared/audiofile.mp3")
    r = requests.post('http://backend:5001/audio')
