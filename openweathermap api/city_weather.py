from datetime import datetime

class City:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def weather_data(self):
        return self.__weather_data

    @weather_data.setter
    def weather_data(self, data):
        result = set({Weather(el) for el in data})
        pass



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
