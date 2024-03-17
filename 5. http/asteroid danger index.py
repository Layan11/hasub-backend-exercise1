import requests
from bs4 import BeautifulSoup as bs

api_key = open("api key.txt")
url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=" + str(api_key)
response = requests.get(url)
data = bs(response.text, 'html.parser')
