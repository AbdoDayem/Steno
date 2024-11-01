import requests
from subprocess import call

old_url = ""
current_url = requests.get('http://0.0.0.0:5001/url').content.decode("UTF-8")
while(True):
    while(old_url == current_url):
        old_url = current_url
        current_url = requests.get('http://0.0.0.0:5001/url').content.decode("UTF-8")
    rc = call("./crawl " + current_url, shell=True)
    old_url = current_url