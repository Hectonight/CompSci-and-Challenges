import urllib.request
from PIL import Image
import os
import requests

fileName = "TempImgAPOD.png"

print("Astronomy Picture of the Day\n")

key = "2fFaAbthV0k3GZogyOkTzgHsOAemZqlPf79OY61t"

response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}").json()
explanation = response["explanation"]
url = response["url"]

print(explanation)

urllib.request.urlretrieve(url, fileName)

img = Image.open(fileName)
img.show()
os.remove(fileName)
