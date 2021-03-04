import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_KEY')


weather_params = {
    "lon": -95.3633,
    "lat": 29.7633,
    'exclude': 'current,minutely,daily',
    'appid': os.environ.get('OWM_API_KEY')
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=weather_params)
response.raise_for_status()
data = response.json()

will_rain = False

for i in range(0,11):
    w_id = data['hourly'][i]['weather'][0]['id']
    if w_id < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="Bring Umbrella",
            from_='+17738256243',
            to='+17133800777'
    )
    print(message.status)


