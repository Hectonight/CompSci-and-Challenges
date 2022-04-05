import tkinter as tk

window = tk.Tk()
window.title("Subway Ticket Price")

tk.Label(text="From Station").grid(row=0, column=0)
tk.Label(text="To Station").grid(row=0, column=1)


def calculate():
    total.set("Total: $" + str(5 * abs(var1.get() - var2.get())))


var1 = tk.IntVar()
var2 = tk.IntVar()
for column in (0, 1):
    for row in range(1, 11):
        tk.Radiobutton(text=str(row), variable=(var1, var2)[column], value=row).grid(row=row, column=column)

total = tk.StringVar()
total.set("Total: $0")
tk.Label(textvariable=total).grid(row=12, column=1)

tk.Button(text="Buy Ticket", command=calculate).grid(row=12, column=0)

window.mainloop()
