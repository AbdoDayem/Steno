import requests
from elasticsearch import Elasticsearch
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
    audioExtensionSet={".mp3",".ogg",".m4a",".flac",".wav"}
    videoExtensionSet={".mp4",".ogg",".wmv",".mov"}
    
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
        esClient.index(index="sourcedownload", id=tag, document=doc)

    #match for extensions
    downloadCollection = set()
    while(audioExtensionSet.__len__() != 0):
        extension = audioExtensionSet.pop()
        resp = esClient.search(index = "sourcedownload",
            query= {"match": 
                    {
                        "audio": extension,
                    }
            }
        )
        #isolates an audio tag containing src
        if(resp.body['hits']['hits'].__len__() != 0):
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
            downloadCollection.add(downloadURL)
    
    while(videoExtensionSet.__len__() != 0):
        extension = videoExtensionSet.pop()
        resp = esClient.search(index = "sourcedownload",
            query= {"match": 
                    {
                        "video": extension,
                    }
            }
        )
        #isolates an audio tag containing src
        if(resp.body['hits']['hits'].__len__() != 0):
            videoTag = resp.body['hits']['hits'][0]['_source']['video']
            downloadTag = ''
            for item in videoTag:
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
            downloadCollection.add(downloadURL)
    
    
    FileDownload(downloadCollection)

    #clear index
    
    esClient.indices.delete(index='sourcedownload')

def FileDownload(urls: set):
    extractedFiles = set()
    while(urls.__len__() != 0):
        url = urls.pop()
        lastDotIndex = 0
        print('\n\n'+url)
        for i in range(url.__len__()):
            if url[i]=='.':
                lastDotIndex = i
        file = url[:lastDotIndex]
        if(not extractedFiles.__contains__(file)):
            extractedFiles.add(file)
            #extension = url[lastDotIndex:lastDotIndex+4]
            destination = 'media/audiofile.mp3'

            urllib.request.urlretrieve(url, destination)

