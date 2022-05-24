import os
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import urllib
import requests


def GetWeatherJson(zip_code):
    zipCodeResponse = requests.get("https://api.zippopotam.us/us/" + zip_code).json()
    place = zipCodeResponse["places"][0]
    lat = place["latitude"]
    long = place["longitude"]
    coordsResponse = requests.get(f"https://api.weather.gov/points/{lat},{long}").json()
    forcastURL = coordsResponse["properties"]["forecast"]
    return requests.get(forcastURL).json()["properties"]["periods"]


def GetWeatherData(periodGoal, periods):
    for dataPeriod in periods:
        if periodGoal == dataPeriod["number"]:
            return dataPeriod
    raise KeyError("period out of range")


def update():
    try:
        weatherPeriods = GetWeatherJson(zipCode.get())
        weatherData = GetWeatherData(int(period.get()), weatherPeriods)
        name.set(weatherData['name'])
        temperature.set(f"{weatherData['temperature']} º{weatherData['temperatureUnit']}")
        windSpeed.set(weatherData['windSpeed'])
        shortForecast.set(weatherData['shortForecast'])
        detailedForecast.set(weatherData['detailedForecast'])
        icon.configure(image=getImageFromURL(weatherData['icon']))

    except KeyError:
        error()
    except ValueError:
        error()


def error():
    name.set("Error")
    temperature.set("Error")
    windSpeed.set("Error")
    shortForecast.set("Error")
    detailedForecast.set("Error")
    icon.configure(image=None)


def getImageFromURL(url):
    filename = "weatherImg.png"
    urllib.request.urlretrieve(url, filename)
    img = Image.open(filename)
    photoImg = ImageTk.PhotoImage(img)
    # os.remove(filename)

    return photoImg


def clear():
    zipCode.set("")
    period.set("")
    name.set("")
    temperature.set("")
    windSpeed.set("")
    shortForecast.set("")
    detailedForecast.set("")
    icon.configure(image=None)


window = Tk()
window.title("Weather")

zipCode = StringVar()
period = StringVar()

name = StringVar()
temperature = StringVar()
windSpeed = StringVar()
shortForecast = StringVar()
detailedForecast = StringVar()

Label(text="Zip Code:").grid(row=0, column=0)
Entry(textvariable=zipCode).grid(row=0, column=1)

Label(text="Period:").grid(row=1, column=0)
Entry(textvariable=period).grid(row=1, column=1)

Label(text="Time:").grid(row=2, column=0)
Label(textvariable=name).grid(row=2, column=1)

Label(text="Temperature:").grid(row=3, column=0)
Label(textvariable=temperature).grid(row=3, column=1)

Label(text="Wind Speed:").grid(row=4, column=0)
Label(textvariable=windSpeed).grid(row=4, column=1)

Label(text="Short Forecast:").grid(row=5, column=0)
Label(textvariable=shortForecast).grid(row=5, column=1)

Label(text="Detailed Forecast:").grid(row=6, column=0)
Label(textvariable=detailedForecast).grid(row=6, column=1)

im = Image.open("weatherImg.png")
im1 = ImageTk.PhotoImage(im)

icon = Label(window, image=im1)
icon.grid(row=7, column=0)

Button(text="Get Weather", command=update).grid(row=8)
Button(text="Clear", command=clear).grid(row=9)

window.mainloop()
