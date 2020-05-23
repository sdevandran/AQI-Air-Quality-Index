import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from calendar import monthrange
import base64
import time
from datetime import datetime

hour = 15
year = 2020
month = 4
s = 1
e = 0 or monthrange(year, month)[1]
fname = f"AQI.csv"
out = open(fname, "a")
print('state,city,station,date,time,PM2.5,PM10,NO2,NH3,SO2,CO,OZONE,AQI,Predominant_Parameter')
print('state,city,station,date,time,PM2.5,PM10,NO2,NH3,SO2,CO,OZONE,AQI,Predominant_Parameter', file=out)

response = requests.post(
    'https://app.cpcbccr.com/aqi_dashboard/aqi_station_all_india', data='e30=', verify='')
for j in [i['stationsInCity'] for i in response.json()['stations']]:
    for k in j:
        # if k['stateID'] == 'Delhi':
            id = k['id']
            for i in list(range(s, e + 1)):
                en = '{' + f'"station_id":"{id}","date":"{year}-{month}-{i}T{hour}:00:00Z"' + '}'
                en = base64.b64encode(en.encode()).decode()
                response = requests.post(
                    'https://app.cpcbccr.com/aqi_dashboard/aqi_all_Parameters', data=en, verify='')
                m = response.json()
                d = datetime.strptime(m['date'], "%A, %d %b %Y %I:%M %p")
                a = {'PM2.5': '0', 'PM10': '0', 'NO2': '0',
                     'NH3': '0', 'SO2': '0', 'CO': '0', 'OZONE': '0'}
                for n in m['metrics']:
                    a[n['name']] = str(n['max'])
                if m['aqi'] and '-' not in a.values():
                    print(f'{k["stateID"]},{k["cityID"]},"{k["name"]}","{d.strftime("%d/%m/%Y")}","{d.strftime("%I:%M:%S %p")}",{",".join(a.values())},{m["aqi"]["value"]},{m["aqi"]["param"]}')
                    print(f'{k["stateID"]},{k["cityID"]},"{k["name"]}","{d.strftime("%d/%m/%Y")}","{d.strftime("%I:%M:%S %p")}",{",".join(a.values())},{m["aqi"]["value"]},{m["aqi"]["param"]}', file=out)
                else:
                    print('error : No Data Available or Insufficient data for', id, k['stateID'],
                          k['cityID'], k['name'], m['title'], d)
out.close()
