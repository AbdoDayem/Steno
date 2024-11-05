import requests
from subprocess import call
import time

old_url = ""
current_url = requests.get('http://backend:5001/url').content.decode("UTF-8")
while(True):
    while(old_url == current_url):
        time.sleep(1)
        old_url = current_url
        current_url = requests.get('http://backend:5001/url').content.decode("UTF-8")
    rc = call("./crawl " + current_url, shell=True)
    old_url = current_url