import os
import requests
import json

path = os.path.realpath(__file__)
path = path[:path.rfind("/") + 1]

while True:
    try:
        SearchInput = input("Search: ")
        url = "https://itunes.apple.com/search?term=" + SearchInput
        response = requests.get(url)
        d = response.json()
        break
    except:
        print("Uh oh! Something went wrong. Please Try Again")


f = open(path + "search-output.json", "w")
f.write(json.dumps(d))
f.close()

tracks = [track for track in d["results"] if track["wrapperType"] == "track"]

for track in tracks:
    print(track["trackName"])

price = str(round(sum([float(track["trackPrice"]) for track in tracks]), 2))

if price[-2] == ".":
    print("$" + price + "0")
else:
    print("$" + price)
