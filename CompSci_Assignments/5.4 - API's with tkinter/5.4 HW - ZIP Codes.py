import tkinter as tk
import requests


def event_lookup():
    try:
        data = requests.get(url + zipCode.get()).json()
        place = data["places"][0]
        city.set(place["place name"])
        state.set(place["state"])
    except:
        city.set("Not a valid ZIP code.")
        state.set("Not a valid ZIP code.")


def event_clear():
    zipCode.set("")
    city.set("")
    state.set("")


url = "https://api.zippopotam.us/us/"

window = tk.Tk()
window.title("ZIP Codes")

# Fill in Entry box and labels here.
# Don't forget three tk.StringVar() variables for the input and the two
# outputs.

zipCode = tk.StringVar()
city = tk.StringVar()
state = tk.StringVar()


tk.Label(text="ZIP Code:").grid(row=0, column=0, sticky="E")
tk.Label(text="Town/city:").grid(row=1, column=0, sticky="E")
tk.Label(text="State:").grid(row=2, column=0, sticky="E")

tk.Entry(textvariable=zipCode).grid(row=0, column=1, columnspan=2)
tk.Label(textvariable=city).grid(row=1, column=1, columnspan=2)
tk.Label(textvariable=state).grid(row=2, column=1, columnspan=2)

tk.Button(text="Look up ZIP Code", command=event_lookup).grid(row=3, column=0, sticky="WE")
tk.Button(text="Clear", command=event_clear).grid(row=3, column=1, sticky="WE")

window.mainloop()
