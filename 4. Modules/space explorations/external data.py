import json
import requests

#ps i did not understand this fully, i was absent in the last week :(

def get_weather(url):
    weather = requests.get(url)
    print(weather.text)