import tkinter as tk


def event_times_two():
    entryString = entryVar.get()
    entryNumber = int(entryString)
    entryNumber *= 2
    entryVar.set(str(entryNumber))


def event_divide_two():
    entryString = entryVar.get()
    entryNumber = int(entryString)
    entryNumber //= 2
    entryVar.set(str(entryNumber))


window = tk.Tk()
window.title("Problem 2: Multiplying and Dividing by 2")

entryVar = tk.StringVar()
tk.Entry(textvariable=entryVar).grid(row=0, column=0, columnspan=2)

tk.Button(text="Multiply", command=event_times_two).grid(row=1, column=0)
tk.Button(text="Divide", command=event_divide_two).grid(row=1, column=1)

window.mainloop()
