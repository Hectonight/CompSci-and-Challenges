import os
from sys import platform
from tkinter import *

window = Tk()
window.title("Hectonite Explorer")


def setpath(file):
    os.chdir(file)
    path.set("Path: " + os.getcwd())
    files.set(os.listdir())


def go():
    index = fileBox.curselection()[0]
    file = files.get()[index]
    try:
        setpath(file)
    except NotADirectoryError:
        os.system("open " + f'"{file}"' if platform != "win32" else "" + f'"{file}"')


def back():
    newPath = os.getcwd()
    temp = newPath[:newPath.rfind("/")]
    if temp != "":
        newPath = temp
    elif platform == "win32":
        return
    else:
        newPath = "/"
    setpath(newPath)


path = StringVar()
files = Variable()
setpath(os.getcwd())
Label(window, textvariable=path).grid(row=0, column=0, sticky=W)

Button(window, text="Back", command=back).grid(row=1, column=0, sticky=W)

fileBox = Listbox(window, listvariable=files)

scrollbar = Scrollbar(window)
fileBox.config(yscrollcommand=scrollbar.set)
fileBox.grid(row=2, column=0, rowspan=4, sticky=N + E + S + W)
fileBox.columnconfigure(0, weight=1)
scrollbar.config(command=fileBox.yview)
scrollbar.grid(row=2, column=2, rowspan=4, sticky=N + S)

fileBox.bind('<Double-1>', lambda event: go())

window.mainloop()
