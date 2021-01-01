# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:27:58 2020

@author: german.santos
"""
import tkinter as tk
import pandas as pd
from tkinter import filedialog

window = tk.Tk()
window.title("Ver archivos")

def LeerArchivo():
    global dff
    fp=filedialog.askopenfilename(title="Select a file",filetypes=(("xlsx files","*.xlsx"),("All  files","*.*")))
#fp = tk.filedialog.askopenfilename()
#fp=tk.filedialog.askopenfilename(title="Select file")
    print("archivo leido")
    print(fp)
    #window.destroy()

    dff = pd.read_excel(fp, engine='openpyxl',sheet_name='Embalse')
    tk.Label(window,text=" Archivo se abríó con éxito",font=('Helvetica', 18), fg='blue').pack()
    tk.Label(window,text=fp,font=16).pack()
btn=tk.Button(window,text="Open File",command=LeerArchivo).pack()
btn2=tk.Button(window,text="Close",command=window.destroy).pack()

#window.destroy()


window.mainloop()