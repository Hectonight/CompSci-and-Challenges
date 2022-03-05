import requests
from math import radians, sqrt, sin, cos, asin

url = "https://api.zippopotam.us/us/"

while True:
    try:
        zip1 = input("Zip Code 1: ")
        zip2 = input("Zip Code 2: ")

        request1, request2 = requests.get(url + zip1), requests.get(url + zip2)
        pos1, pos2 = request1.json(), request2.json()

        pos1["places"]
        pos2["places"]
        break

    except:
        print("At least one of those zip codes were not real")

lat1 = radians(float(pos1['places'][0]['latitude']))
long1 = radians(float(pos1['places'][0]['longitude']))
lat2 = radians(float(pos2['places'][0]['latitude']))
long2 = radians(float(pos2['places'][0]['longitude']))

print("Distance: "
      + str(7917.6 * asin(sqrt(sin((lat1 - lat2) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((long1 - long2) / 2) ** 2)))
      + " miles")
