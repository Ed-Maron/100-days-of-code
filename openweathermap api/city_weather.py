from datetime import datetime
from  requests import get 

appid = "3e6f7c567fcc226aa6b7ab089fd6380e"
class City:

    def __init__(self, name):
        self.__name = name
        self.__weather = []

        self.get_coord()
        self.get_weather_last_5days()

    def get_coord(self):
        try:
            res = get("http://api.openweathermap.org/data/2.5/find",
                        params={'q':self.name, 'units': 'metric', 'APPID': appid})
            data = res.json()
            self.__coord=data['list'][0]['coord']
        except Exception as e:
            self.__msg = e

    def get_weather_last_5days(self):
            try:
                res = get("http://api.openweathermap.org/data/2.5/onecall/timemachine",
                    params={'lat':self.coord['lat'], 'lon': self.coord['lon'],'dt':'1642275329', 'APPID': appid})
                data = res.json()
                
                self.weather.append(Weather(data))
            except Exception as e:
                print("Exception (find):", e)

    @property
    def name(self):
        return self.__name

    @property
    def coord(self):
        return self.__coord

    @property
    def weather(self):
        return self.__weather

    @property
    def msg(self):
        return self.__msg



class Weather:

    def __init__(self, info):
        self.__date_log = datetime.today()
        self.__temp = 0
        self.__feels_like  = 0
        self.__humidity = 0 
        self.__visibility = 0
 
    #getters       
    @property
    def temp(self):
        return self.__temp

    @property
    def date_log(self):
        return self.__date_log

    @property
    def feels_like(self):
        return self.__feels_like   
    
    @property
    def humidity(self):
        return self.__humidity

    @property
    def visibility(self):
        return self.__visibility
