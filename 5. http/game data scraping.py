import http.client

# Create an HTTPS connection to example.com
import json

import requests

conn = http.client.HTTPSConnection("store.steampowered.com")
# Send a GET request to the root path ("/")
# conn.request("GET", "/charts/topselling/global")
# conn.request("GET", "/search/results")
# conn.request("GET", "/search/?tags=")
conn.request("GET", "/search/?supportedlang=english&ndl=1")

# Get the response
response = conn.getresponse()
data = response.read().decode("utf-8")
print(data)


# from bs4 import BeautifulSoup
#
# parsed_html = BeautifulSoup(data)
# print(parsed_html.body.find('div', attrs={'class':'container'}).text)

import re

match = re.search(r'<span class="title">(.*?)</span>', data)

if match:
      title = match.group(1)
      print("Website Title:", title)
# # Print the response status code and reason
# print(f"Status Code: {response.status}")
# print(f"Reason: {response.reason}")
#
# data = response.read().decode("utf-8")
# print("Received data:", data)
# # print()

# import json
# import urllib.request
#
# response = urllib.request.urlopen("https://store.steampowered.com/")
# text = response.read()
# print(json.loads(text.decode('utf-8')))


# r = requests.get("store.steampowered.com/charts/topselling/global")
# print(r.text)
