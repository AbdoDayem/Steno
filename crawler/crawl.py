import requests
from subprocess import call


old_url = ""
current_url = requests.get('http://localhost:5000/url').content.decode("UTF-8")
print(current_url)
while(old_url == current_url):
    old_url = current_url
    current_url = requests.get('http://localhost:5000/url').content.decode("UTF-8")

rc = call("./crawl " + current_url, shell=True)