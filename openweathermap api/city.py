from tkinter import ACTIVE
from  requests import get 
from datetime import datetime, timedelta
from weather import Weather
import matplotlib.pyplot as plt

appid = "3e6f7c567fcc226aa6b7ab089fd6380e"
class City:
    LAST_IMG_INDEX = 1
    curent_date = datetime.now()

    def __init__(self, name):
        self.__name = name
        self.__weather = []

        self.get_coord()
        self.get_weather()

    def get_coord(self):
        try:
            res = get("http://api.openweathermap.org/data/2.5/find",
                        params={'q':self.name, 'units': 'metric', 'APPID': appid})
            data = res.json()
            self.__coord=data['list'][0]['coord']
        except Exception as e:
            self.__msg = e

    def get_weather(self):
            try:
                res = get("http://api.openweathermap.org/data/2.5/onecall/timemachine",
                    params={'lat':self.coord['lat'], 
                            'lon': self.coord['lon'],
                            'dt': int(datetime.timestamp(self.curent_date)), 
                            'APPID': appid}
                )
                data = res.json()
                
                self.__weather = [Weather(el) for el in data['hourly']]
                self.__weather.append(Weather(data['current']))
            except Exception as e:
                print("Exception (find):", e)


    def show_feels_like_data(self):
        data = self.__weather
        
    #    temp_data = {
    #        "x":[i for i in range(len(data))],
    #        "y":[el.temp[0] for el in data]
    #   }

        feels_like_data = {
            "x":[i for i in range(len(data))],
            "y":[el.feels_like[0] for el in data]
        }
        plt.ion()
        plt.title("Feels like versus time")
        plt.xlabel("Hour")
        plt.ylabel("Temp")
        plt.grid() 
        plt.subplot(2, 2, self.LAST_IMG_INDEX)
        plt.plot(feels_like_data['x'], feels_like_data['y'])
        
        self.LAST_IMG_INDEX+=1
        pass

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




