# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:30:00 2018

@author: USER
"""

from pprint import pprint
import urllib.request, json
import numpy as np
url = "http://opendata2.epa.gov.tw/AQI.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
#print(data[0])
"""
print(len(data))

for i in range(0,len(data)-1):
       if str(data[i]['County']) == str("屏東縣"):
              pprint("ID: %d,   County: %s" %(i,data[i]['SiteName']))
"""
station_id=57

if not data[station_id]['PM2.5']:
       pm25='-99.00'
else:
       pm25=data[station_id]['PM2.5']
       
if not data[station_id]['PM10']:
       pm10='-99.00'
else:
       pm10=data[station_id]['PM10']

if not data[station_id]['CO']:
       CO='-99.00'
else:
       CO=data[station_id]['CO']

if not data[station_id]['PM2.5']:
       SO2='-99.00'
else:
       SO2=data[station_id]['SO2']

if not data[station_id]['O3']:
       O3='-99.00'
else:
       O3=data[station_id]['O3']
if not data[station_id]['WindDirec']:
       WindDirection='-99'
else:
       WindDirection=data[station_id]['WindDirec']

if not data[station_id]['WindSpeed']:
       WindSpeed='-99.00'
else:
       WindSpeed=data[station_id]['WindSpeed']

#output="SiteName: %s, PM2.5: %s, PublishTime: %s" %(data[0]['SiteName'], data[0]['PM2.5'], data[0]['PublishTime'])
output=list([pm25,pm10,CO,SO2,O3,WindDirection,WindSpeed,data[station_id]['PublishTime'].replace(" ","-")])
#print(output)
exit(output)

