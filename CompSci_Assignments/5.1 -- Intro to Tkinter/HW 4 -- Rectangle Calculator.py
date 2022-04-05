import tkinter as tk

window = tk.Tk()
window.title("Problem 4: Rectangle Calculator")


def calc():
    try:
        aVar.set(int(lVar.get())*int(wVar.get()))
        pVar.set(2 * int(lVar.get()) + 2 * int(wVar.get()))
    except:
        aVar.set("Error")
        pVar.set("Error")


def clear():
    lVar.set("")
    wVar.set("")
    aVar.set("")
    pVar.set("")


tk.Label(text="Length:").grid(row=0, column=0, sticky="E")
tk.Label(text="Width:").grid(row=1, column=0, sticky="E")
tk.Label(text="Area:").grid(row=2, column=0, sticky="E")
tk.Label(text="Perimeter:").grid(row=3, column=0, sticky="E")

lVar = tk.StringVar()
wVar = tk.StringVar()
tk.Entry(textvariable=lVar).grid(row=0, column=1)
tk.Entry(textvariable=wVar).grid(row=1, column=1)

aVar = tk.StringVar()
pVar = tk.StringVar()
tk.Label(textvariable=aVar).grid(row=2, column=1)
tk.Label(textvariable=pVar).grid(row=3, column=1)
tk.Button(text="Calculate", command=calc).grid(row=4, column=0)
tk.Button(text="Clear", command=clear).grid(row=4, column=1, sticky="WE")

window.mainloop()
