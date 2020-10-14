# Digital-Clock-With-Python

#pip install tkinter
from tkinter import *
from tkinter.ttk import * 
from time import strftime

root = Tk()
root.title("Clock By Lakshay Mahajan!")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(700, time)

label = Label(root, font=("ds-digital", 45), background = "black", foreground = "cyan")
label.pack(anchor = 'center')
time()

mainloop()
