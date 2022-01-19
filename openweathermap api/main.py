from unicodedata import name
from  requests import get 
from city_weather import City 

cities = ["Petersburg","Moscow"]
appid = ""

cities_id = dict()

for city in cities:
    try:
        res = get("http://api.openweathermap.org/data/2.5/find",
                    params={'q':city, 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities_id[data['list'][0]['name']]=data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)

result = dict()
for key in cities_id:
    try:
        res = get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id':cities_id[key], 'units': 'metric', 'APPID': appid})
        data = res.json()
        result[key]=data
    except Exception as e:
        print("Exception (find):", e)
        
print(result['Moscow'])

res = get("http://api.openweathermap.org/data/2.5/onecall/timemachine",
                    params={'lat':'60.99', 'lon': '30.9', 'APPID': appid, 'dt':'1642275329'})
data = res.json()
print(data)