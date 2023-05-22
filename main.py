import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "youremail@gmail.com"
APP_PASSWORD = "your_password"

# ISS API

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

ISS_LAT = float(data['iss_position']['latitude'])
ISS_LNG = float(data['iss_position']['longitude'])

# Time

time_now = dt.datetime.now()

# Sunrise / Sunset API
NEW_LAT = 47.425433
NEW_LNG = 15.432532

MY_LAT = 55.676098
MY_LNG = 12.568337
# print(MY_LAT, MY_LNG)
print(ISS_LAT, ISS_LNG)
print(NEW_LAT, NEW_LNG)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise_result = int(data['results']['sunrise'].split("T")[1].split(":")[0])
# sunrise_result = data['results']['sunrise']
# print(sunrise_result.split("T")[1].split(":"))
# print(sunrise_result)

sunset_result = int(data['results']['sunset'].split("T")[1].split(":")[0])
# sunset_result = data['results']['sunset']
# print(sunset_result)
# print(time_now.hour)

# Logic
time.sleep(60)
if round(NEW_LAT) in range(round(ISS_LAT - 5), round(ISS_LAT + 5)) and round(NEW_LNG) in range(round(ISS_LNG - 5),
                                                                                             round(ISS_LNG + 5)):
    if time_now.hour >= sunset_result or time_now.hour <= sunrise_result:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="arthurmalone13@yahoo.com",
                msg="Subject:ISS is just above you\n\nIf you look into the stars you might will see the ISS satellite."
            )
else:
    print("nothing")
