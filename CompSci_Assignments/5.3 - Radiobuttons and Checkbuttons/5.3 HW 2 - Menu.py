import tkinter as tk

window = tk.Tk()
window.title("Menu")

tk.Label(text="Choose any combination of items").grid(row=0, column=0)


# Add check buttons and IntVar's here. All Checkbutton commands are calculate
def calculate():
    total = 10 * Sandwich.get() + 2 * Apple.get() + 3 * Drink.get() - (Sandwich.get() and Apple.get() and Drink.get())
    totalVar.set("Total price: $" + str(total))


Sandwich = tk.BooleanVar()
Apple = tk.BooleanVar()
Drink = tk.BooleanVar()

for index, (name, var) in enumerate(zip(["Sandwich", "Apple", "Drink"], [Sandwich, Apple, Drink])):
    tk.Checkbutton(text=name, variable=var, command=calculate).grid(row=index + 1, column=0, sticky="W")

totalVar = tk.StringVar()
totalVar.set("Total price: $")
tk.Label(textvariable=totalVar).grid(row=4, column=0, sticky="WE")

window.mainloop()
