import tkinter as tk
from tkinter import ttk

# Add a single event handler here


window = tk.Tk()
window.title("Homework problem 1")

prices = {"Sandwich": 9.99, "Drink": 2.49, "Cookies": 1.99}


# Add Spinboxes and other code here.
def update():
    resultVar.set("$" + str(round((prices[foodVar.get()] * countVar.get()), 2)))


resultVar = tk.StringVar()
tk.Label(textvariable=resultVar).grid(row=2, column=0, padx=5, pady=5)

foodVar = tk.StringVar()
foodVar.set(list(prices)[0])
ttk.Spinbox(textvariable=foodVar, command=update, values=list(prices.keys())).grid(row=0, column=0, padx=10, pady=10)

countVar = tk.IntVar()
countVar.set(1)
ttk.Spinbox(textvariable=countVar, command=update, values=list(range(1, 5))).grid(row=1, column=0, padx=10, pady=10)

window.mainloop()
