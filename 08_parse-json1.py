import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?"
orig = "Kiev"
dest = "London"
key = "nx6L2yvG2qBBYY9cnB4RXshWv4vTitHu"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print(url)
json_data = requests.get(url).json()
print(json_data)