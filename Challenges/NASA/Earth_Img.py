import urllib
from PIL import Image
from datetime import date
import os
import requests

print("Most Recent Picture of the Earth")

fileName = "TempImgEarth.png"
response = requests.get("https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY").json()
data = response[-1]
image = data["image"]
dateTaken = data["date"]
dateTaken = dateTaken[:dateTaken.find(" ")].replace("-", "/")

urllib.request.urlretrieve("https://api.nasa.gov/EPIC/archive/natural/"
                           f"{dateTaken}/png/{image}.png?api_key=2fFaAbthV0k3GZogyOkTzgHsOAemZqlPf79OY61t",
                           fileName)

img = Image.open(fileName)
img.show()
os.remove(fileName)