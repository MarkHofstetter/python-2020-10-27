import requests
import pprint

url = 'https://data.bka.gv.at/ris/api/v2.5/bundesgesetzblaetter'

response = requests.get(url)
if response.status_code != 200:
    exit()

data = response.json()
pprint.pprint(data)

# print("akutelle Temperatur {:.1f}".format(data['main']['temp'] - 273.15))