#!/usr/bin/env python3
"""
API testing with ds api
"""
import json
import requests


def get_weather():
    """
    this
    """
    k = ""
    url = "https://api.darksky.net/forecast/"
    lat = 43.6591
    lon = 70.2568

    data = requests.get(f"{url}{k}/{lat},{lon}")
    json_data = json.loads(data.text)
    today = json_data["daily"]["data"][0]
    high = today["temperatureHigh"]
    low = today["temperatureLow"]

    return f"Today - High: {high}, Low: {low}"


weather = get_weather()
print(weather)
