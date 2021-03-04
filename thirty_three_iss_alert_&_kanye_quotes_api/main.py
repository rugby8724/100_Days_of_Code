import requests
from datetime import datetime

MY_LAT = 29.7422
MY_LNG = -95.4084

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (latitude, longitude)
#
# print(iss_position)
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
results = data['results']
sunrise = int(results['sunrise'].split('T')[1].split(':')[0])
sunset = (results['sunset'].split('T')[1].split(':')[0])
day_length = results['day_length']
print(sunrise)
print(sunset)
print((day_length/60)/60)

time_now = datetime.now()
print(time_now.hour)