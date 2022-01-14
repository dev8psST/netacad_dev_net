import urllib.parse
import requests
from time import gmtime, strftime
from datetime import datetime


url = "https://api.sunrise-sunset.org/json?lat=48.8584&lng=2.2945"
#url2 = "https://maps.googleapis.com/maps/api/timezone/json?location=48.8584,2.2945&timestamp=1458000000"

json_data = requests.get(url).json()
#json_data2 = requests.get(url2).json()

print("Sunrise Paris: " + json_data["results"]["sunrise"])
print("Sunset Paris: " + json_data["results"]["sunset"])

print(strftime("%z", gmtime()))
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print(type(current_time))
