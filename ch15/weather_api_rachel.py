# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:36:32 2019

@author: winkl
"""

import config

#######################################
"""Task Two: APIs using Weather map"""
#######################################

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":config.weather_api_key}

response = requests.get(endpoint, params=payload)
data = response.json() #in a json format

print('This is what data looks like\n')
print(data)

print (response.url)
print(response.status_code)
print(response.headers["content-type"])