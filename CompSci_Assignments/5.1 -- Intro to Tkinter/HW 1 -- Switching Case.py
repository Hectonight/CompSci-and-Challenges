import tkinter as tk


def event_to_upper():
    entryString = entryVar.get()
    entryString = entryString.upper()
    entryVar.set(entryString)


def event_to_lower():
    entryString = entryVar.get()
    entryString = entryString.lower()
    entryVar.set(entryString)


window = tk.Tk()
window.title("Problem 1: Switching case")

entryVar = tk.StringVar()
tk.Entry(textvariable=entryVar).grid(row=0, column=0, columnspan=2)

tk.Button(text="UPPER", command=event_to_upper).grid(row=1, column=1)
tk.Button(text="LOWER", command=event_to_lower).grid(row=1, column=0)

window.mainloop()
