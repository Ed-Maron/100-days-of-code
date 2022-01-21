from  requests import get 
from datetime import datetime, timedelta
from weather import Weather

appid = "3e6f7c567fcc226aa6b7ab089fd6380e"
class City:
    curent_date = datetime.now()
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
                    params={'lat':self.coord['lat'], 
                            'lon': self.coord['lon'],
                            'dt': int(datetime.timestamp(self.curent_date+timedelta(days=-4))), 
                            'APPID': appid}
                )
                data = res.json()
                
                self.__weather = [Weather(el) for el in data['hourly']]
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




