import os
import json

path = os.path.realpath(__file__)
path = path[:path.rfind("/")+1]


f = open(path + "university-data.json", "r")
unis = json.loads(f.read())
f.close()

col = input("Enter the name of a college. ").title()
# Fix search up
for uni in unis:
    if col in uni["name"]:
        print(uni["name"])
        print(uni["web_pages"][0])
        exit()


print("Could not find university")

