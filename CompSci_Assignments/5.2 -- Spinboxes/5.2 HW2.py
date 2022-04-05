import tkinter as tk
from tkinter import ttk


# Add a single event handler here.
def update():
    office.set(employees[employee.get()])
    phone.set(phones[int(office.get())])


window = tk.Tk()
window.title("Homework problem 2")

employees = {"Alice": 109, "Bob": 208, "Cindy": 307, "Dan": 406}
phones = {406: 1234, 307: 5678, 208: 8421, 109: 9753}

tk.Label(text="Employee").grid(row=0, column=0, padx=5, pady=5)
tk.Label(text="Office").grid(row=0, column=1, padx=5, pady=5)
tk.Label(text="Phone extension").grid(row=0, column=2, padx=5, pady=5)

office = tk.StringVar()
tk.Label(textvariable=office).grid(row=1, column=1, padx=5, pady=5)

phone = tk.StringVar()
tk.Label(textvariable=phone).grid(row=1, column=2, padx=5, pady=5)

employee = tk.StringVar()
employee.set(list(employees)[0])
ttk.Spinbox(textvariable=employee, command=update, values=list(employees.keys())).grid(row=1, column=0, padx=10,
                                                                                       pady=10)
# Add Spinboxes, labels, and other code here.


window.mainloop()
