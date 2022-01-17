from  requests import get 
s_city = "Petersburg"
city_id = 0
appid = "MyAppId"

#Find city Id
try:
    res = get("http://api.openweathermap.org/data/2.5/find",
                 params={'q':s_city, 'units': 'metric', 'APPID': appid})
    data = res.json()
    city_id = data['list'][0]['id']
except Exception as e:
    print("Exception (find):", e)

#request data by city_id
try:
    res = get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id':city_id, 'units': 'metric', 'APPID': appid})
    data = res.json()

    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
