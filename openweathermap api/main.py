from asyncio.windows_events import NULL
from unicodedata import name
from  requests import get 
from city import City 


cities = ["Petersburg","Moscow"]

result = [City(name) for name in cities]

first_city = result[0]
first_city.show_feels_like_data()
first_city.show_feels_like_data()

second_city = result[1]
second_city.show_feels_like_data()
second_city.show_feels_like_data()


pass