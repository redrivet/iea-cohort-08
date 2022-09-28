#!/bin/env python3

"""Replicate this with requests instead of urllib"""

# from urllib.request import urlopen
# SECRET_KEY = '1d8c58ed1d54f96f939e706c788650f1'

# lat, long = (33.8840,-84.5144)  # Smyrna, GA

# url = 'https://api.darksky.net/forecast/{key}/{lat},{long}'.format(
#     key=SECRET_KEY, lat=lat, long=long)
# response = urlopen(url)  # Defaults to a GET request
# # Returns a file-like Response object, so we can read it just like File I/O
# print(response)
# print(dir(response))

from pprint import pprint
import requests

SECRET_KEY = '1d8c58ed1d54f96f939e706c788650f1'
lat , long = (47.67, -117.40) # Spokane, WA
response = requests.get('https://api.darksky.net/forecast/{key}/{lat},{long}'.format(key=SECRET_KEY, lat=lat, long=long))

response_dict = response.json()

pprint(response_dict)



# for row in response:
#     print(row[lat],row[long])
