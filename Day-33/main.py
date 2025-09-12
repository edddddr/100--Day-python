import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "endt6342@gmail.com"
MY_PASSWORD = "cnbqubgpmobilcjt"

MY_LAT = 51.507351
MY_LONG = -0.127758

def is_iss_over_head():

    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT+5 <= iss_latitude <= MY_LAT-5 and MY_LONG+5 <= iss_longitude <= MY_LONG-5:
        return True

def is_night():
    parametrs = {
            'lat': MY_LAT,
            'lng': MY_LONG,
            'formatted': 0,
        }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parametrs)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_over_head() and is_night():
         with smtplib.SMTP("smtp.gmail.com") as connections:
            connections.starttls()
            connections.login(user=MY_EMAIL, password=MY_PASSWORD)
            connections.sendmail(from_addr=MY_EMAIL, to_addrs="ermiasthomas9@gmail.com", msg=f"subject: Time\n\nNight Time")

