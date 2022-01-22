from asyncio.windows_events import NULL
from unicodedata import name
from  requests import get 
from city import City 


cities = ["Petersburg","Moscow"]

result = [City(name) for name in cities]

first_city = result[0]
first_city.display_diagram_temp_hourly()
pass