# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:30:00 2018

@author: USER
"""

import urllib.request, json

url = "http://opendata2.epa.gov.tw/AQI.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
if not data[0]['PM2.5']:
       pm25='-99999'
else:
       pm25=data[0]['PM2.5']

output=list([pm25,data[0]['PublishTime'].replace(" ","-")])
#print(output)
exit(output)

