#!/bin/bash
keelung=($(python3.6 ~/python_code/keelung.getAQI.0515.py 2>&1 |  tr -d "[] '"| tr "," " " ))
meinong=($(python3.6 ~/python_code/meinong.getAQI.0515.py 2>&1 |  tr -d "[] '"| tr "," " " ))
pingtung=($(python3.6 ~/python_code/pingtung.getAQI.0515.py 2>&1 |  tr -d "[] '"| tr "," " " ))

DATE=$(date +%Y-%m-%d-%H-%M)
mysql -u borden -pwufunchen1996 <<EOFMYSQL
USE AQI_data;
INSERT INTO meinong(PM25,PM10,CO,SO2,O3,WindDirection,WindSpeed,Publishtime) 
VALUES (${meinong[0]},${meinong[1]},${meinong[2]},${meinong[3]},${meinong[4]},${meinong[5]},${meinong[6]},'${meinong[7]}');
INSERT INTO pingtung(PM25,PM10,CO,SO2,O3,WindDirection,WindSpeed,Publishtime)
VALUES (${pingtung[0]},${pingtung[1]},${pingtung[2]},${pingtung[3]},${pingtung[4]},${pingtung[5]},${pingtung[6]},'${pingtung[7]}');


EOFMYSQL
