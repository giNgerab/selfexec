import os
from tkinter import *
from tkinter import ttk

def zopa():
    i=10
    while (i>1):
        os.system('start pipiska.exe')
        i=i-1

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=zopa).grid(column=1, row=0)
root.mainloop()
