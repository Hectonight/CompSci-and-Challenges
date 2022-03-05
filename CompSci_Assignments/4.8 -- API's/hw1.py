import os
import requests
import json

path = os.path.realpath(__file__)
path = path[:path.rfind("/") + 1]

participants = input("How many participants are there? ")
url = "https://www.boredapi.com/api/activity/?participants=" + participants
response = requests.get(url)
d = response.json()
print(d["activity"])
