import urllib.request as urlReq
import requests

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

def ElasticSearch():
    print('not yet implemented')

def FileDownload():
    print('not yet implemented')

