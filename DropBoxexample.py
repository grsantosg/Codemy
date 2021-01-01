# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:27:58 2020

@author: german.santos
"""
import tkinter as tk



window = tk.Tk()
window.geometry('200x150')
window.title("Seleccionar caja")



def showdrop():
     tk.Label(window,text=clicked.get()).pack()
     
options=[
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado"
    ]
    
clicked=tk.StringVar()
clicked.set(options[0])
drop=tk.OptionMenu(window,clicked,*options)
drop.pack()
btn3=tk.Button(window,text="Show Selecction",command=showdrop).pack()
btn2=tk.Button(window,text="Close",command=window.destroy).pack()

#window.destroy()


window.mainloop()