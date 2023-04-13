import requests
country = input('Enter country:')
res = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={country}')
res = res.json()['results']
res = res[1]
latitude = res['latitude']
longitude = res['longitude']
geo = requests.get(f'https://api.open-meteo.com/v1/forecast?&forecast_days=1&latitude={latitude}&longitude={longitude}&hourly=temperature_2m')
geo = geo.json()
geo = geo['hourly']
key = geo['time']
temp = geo['temperature_2m']
print(f'The air temperature today is from {temp[0]} to {temp[23]} degrees')