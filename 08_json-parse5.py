import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?"
key = "nx6L2yvG2qBBYY9c###nB4RXshWv4vTitHu"

while True:

    orig = input("Starting location: ")
    dest = input("Destination: ")



    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest,
                                             "unit":"k", "locale":"ru_RU"})

    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n ")
        print(f"Direction from {orig} to {dest}")
        print("Trip duration: " + json_data["route"]["formattedTime"])
        print("Kilometers:      " + str((json_data["route"]["distance"])))
        print("Fuel Used (Ltr): " + str((json_data["route"]["fuelUsed"])*3.78))

        print("="*35)
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + "(" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("="*35+"\n")

    elif json_status == 402:
        print("\n"+"*"*35)
        print("Status code: " + str(json_status) +
              "; Invalid user inputs for one or both locations. ")
        print("\n"+"*"*35)

    else:
        print("\n"+"*"*35)
        print("Status code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("\n"+"*"*35)
    if "q" ==  input("quit? >> q or Enter: "):
        print("QUIT bye")
        break
