# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:51:56 2021

@author: german.santos
"""
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

window = tk.Tk()

window.title("Graficas con tkinter")
window.geometry("400x200")

def graph():
    house=np.random.normal(200000,25000,5000)
    plt.hist(house,50)
    plt.show()
    

my_button=tk.Button(window,text="Gráfica",command=graph)
my_button.pack()

#canvas = FigureCanvasTkAgg(fig, master=window)
#canvas.draw()
#canvas.get_tk_widget().place(x=300, y=370)
window.mainloop()


house=np.random.normal(200000,25000,5000)
plt.hist(house,50)
plt.show()