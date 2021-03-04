import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_email = 'tadtesting24@gmail.com'
password = 'Onehundred100'

#If the ISS is close to my current position
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    # and it is currently dark
    return time_now.hour >= sunset


while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(900)
    if is_iss_overhead() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP('smtp.google.com', 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs='tadtesting24@yahoo.com', msg='Subject:ISS Above\n\n '
                                                                                           'Look up!')




