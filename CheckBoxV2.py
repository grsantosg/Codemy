# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:27:58 2020

@author: german.santos
"""
import tkinter as tk



window = tk.Tk()
window.title("Seleccionar caja")

def show():
    
    tk.Label(window,text=var.get()).pack()
    
var=tk.StringVar()

c=tk.Checkbutton(window,text="Check this box",variable=var,onvalue="On",offvalue="Off")
c.deselect()
c.pack()
btn=tk.Button(window,text="Show Selecction",command=show).pack()


btn2=tk.Button(window,text="Close",command=window.destroy).pack()

#window.destroy()


window.mainloop()