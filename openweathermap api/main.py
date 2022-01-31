from asyncio.windows_events import NULL
from unicodedata import name
from  requests import get 
from city import City 


cities = ["Petersburg","Moscow"]

result = [City(name) for name in cities]

first_city = result[0]
first_city.show_split_diagramm()
first_city.show_feels_like_diagram()
pass