import tkinter as tk


def event_find_max():
    try:
        stringA = aVar.get()
        numA = int(stringA)
        stringB = bVar.get()
        numB = int(stringB)

        outputVar.set(max(numA, numB))
        # (B) Complete the event handler so that the greatest number
        # from the two Entry boxes is displayed in your new label.
    except:
        outputVar.set("Error")
        # (C) In this part, display "ERROR" in the "output" label.


window = tk.Tk()
window.title("Problem 3: Finding a max value")

aVar = tk.StringVar()
tk.Entry(textvariable=aVar).grid(row=0, column=0)

bVar = tk.StringVar()
tk.Entry(textvariable=bVar).grid(row=0, column=1)


tk.Label(text="Max value:").grid(row=1, column=0)

outputVar = tk.StringVar()
tk.Label(textvariable=outputVar).grid(row=1, column=1, sticky="W")
# (A) Create a Label here, along with its own StringVar. Should go at Row 1, Column 1, to the right of "Max Value:"

tk.Button(text="Find Max", command=event_find_max).grid(row=2, column=0, columnspan=2, sticky="WE")

window.mainloop()
