from tkinter import *
from tkinter import ttk
import tkinter as tk

i=10

def zopa(i, button, text):
    button.destroy()
    if(i>0):
        button = ttk.Button(frm, text = f"{i} more pressings", command= lambda: zopa(i, button, text))
        button.grid(column = 1, row = 0)
        i = i-1
        return
    button = ttk.Label(frm, text = text.get())
    button.grid(column = 1, row = 0)
    print(text)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

text = tk.StringVar()
entry = ttk.Entry(root, textvariable = text, justify = CENTER)
button = ttk.Button(frm, text="PENIS", command= lambda: zopa(i, button, text))

entry.focus_force()
entry.grid(column = 0, row = 1)
button.grid(column = 1, row = 1)

root.mainloop() 
