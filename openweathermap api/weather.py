from datetime import datetime

class Weather:

    def __init__(self, info):
        self.__date_log = info['dt']
        self.__temp = info['temp']
        self.__feels_like  = info['feels_like']
        self.__humidity = info['humidity']
        self.__visibility = info['visibility']
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