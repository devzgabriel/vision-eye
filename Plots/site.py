import requests
import urllib, json

x = requests.get('https://tender-hermann-50fe63.netlify.app/')
js = x.json()
print (js)

#url = "https://tender-hermann-50fe63.netlify.app/"
#response = urllib.request.urlopen(url)
#data = json.loads(response.read())
#print(data)
"""url = "https://tender-hermann-50fe63.netlify.app"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print (data)"""
