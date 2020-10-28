import requests
import pprint

url = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'

response = requests.get(url)
if response.status_code != 200:
    exit()

data = response.json()
# pprint.pprint(data)

print("akutelle Temperatur {:.1f}".format(data['main']['temp'] - 273.15))