# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:07:11 2020

@author: german.santos
"""
import tkinter as tk
import sqlite3 as sq3
import requests
import json

#https://www.airnowapi.org/aq/forecast/zipCode/?format=text/csv&zipCode=20002&date=2020-12-31&distance=25&API_KEY=6F8456CE-D9ED-4E41-B074-8D515DA79E93

window = tk.Tk()

window.title("Weather API")
window.geometry("600x100")

#def ziplookup():
    #zip.get()
    #zipLabel=tk.Label(window,text=zip.get())
    #zipLabel.grid(row=1,column=0,columnspan=2)
#
  
try:
    api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60007&distance=25&API_KEY=6F8456CE-D9ED-4E41-B074-8D515DA79E93")
    api=json.loads(api_request.content)
    city=api[0]['ReportingArea']
    qual=api[0]['AQI']
    cate=api[0]['Category']['Name']
    print(city)
    if cate=="Good":
        wcolor="#0C0"
    elif cate=="Moderate":
        wcolor="#FFF00"
    elif cate=="Unhealthy for Sensitive Groups":
        wcolor="#ff9900"
    elif cate=="Unhealhty":
        wcolor="#FF0000"
    elif cate=="Very Unhealthy":
        wcolor="#990066"
    elif cate=="Hazardous":
        wcolor="#660000"
        
    window.configure(bg=wcolor) 
    #myLabel=tk.Label(window,text=api[0])
    myLabel=tk.Label(window,text=city+"  Air Quality  "+str(qual)+" "+cate,font="Helvetica,20",bg=wcolor)
    #print(api[0])
    
    #myLabel.grid(row=1,colum=1)
    myLabel.pack()

except Exception as e:
    api="Error..."


window.mainloop()