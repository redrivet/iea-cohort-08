#!/usr/bin/env python3

"""Basic example of using 'requests' to get geolocation info."""

import requests

ip_address = input('Enter an IP address to search:  ')
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
print(result)
