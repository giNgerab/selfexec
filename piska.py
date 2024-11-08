import subprocess
import os
from tkinter import *
from tkinter import ttk

def zopa():
        subprocess.run(["chmod +x piska", "-l"])
    i=10
    while (i>1):
         subprocess.run(["./piska", "-l"])
         i=i-1

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=zopa).grid(column=1, row=0)
root.mainloop()
