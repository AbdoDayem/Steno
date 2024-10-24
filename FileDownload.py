import urllib.request as urlReq
import requests
import elasticsearch as es

def HtmlAcquisition(url: str):

    #urllib
    pageAccess = urlReq.urlopen(url)
    pageBytes = pageAccess.read()
    pageHtml = pageBytes.decode("utf8")
    pageAccess.close()

    #requests
    pageAccess2 = requests.get(url)
    
    pageAccess2.text
    #requires RFC2616

    ElasticSearch()

def ElasticSearch(url: str, html: str):
    esClient = es('https://localhost:9200', api_key='certs/ca-cert.pem') #add password
    esClient.indicies.create(url)
    
    print('not yet implemented')

def FileDownload():
    print('not yet implemented')

