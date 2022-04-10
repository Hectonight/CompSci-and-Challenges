import os
from sys import platform
from tkinter import *

window = Tk()
window.title("Hectonite Explorer")


def setpath():
    path.set("Path: " + os.getcwd())
    files.set(os.listdir())


def go():
    index = fileBox.curselection()[0]
    file = files.get()[index]
    try:
        os.chdir(file)
        setpath()
    except NotADirectoryError:
        os.system("open " + f'"{file}"' if platform != "win32" else "" + f'"{file}"')


path = StringVar()
files = Variable()
setpath()
Label(window, textvariable=path).grid(row=0, column=0, sticky=W)

fileBox = Listbox(window, listvariable=files)

scrollbar = Scrollbar(window)
fileBox.config(yscrollcommand=scrollbar.set)
fileBox.grid(row=1, column=0, rowspan=4, sticky=N + E + S + W)
fileBox.columnconfigure(0, weight=1)
scrollbar.config(command=fileBox.yview)
scrollbar.grid(row=1, column=2, rowspan=4, sticky=N + S)

fileBox.bind('<Double-1>', lambda event: go())

window.mainloop()
