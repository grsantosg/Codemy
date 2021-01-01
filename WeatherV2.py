# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:07:11 2020

@author: german.santos
"""
import tkinter as tk
import sqlite3 as sq3
import requests
import json


window = tk.Tk()

window.title("Weather API")
window.geometry("600x100")



def ziplookup():
    #zip.get()
    #zipLabel=tk.Label(window,text=zip.get())
    #zipLabel.grid(row=1,column=0,columnspan=2)
#

    try:
        api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=25&API_KEY=6F8456CE-D9ED-4E41-B074-8D515DA79E93")
        #api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=25&API_KEY=6F8456CE-D9ED-4E41-B074-8D515DA79E93")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        qual=api[0]['AQI']
        cate=api[0]['Category']['Name']
        #print(city)
        #print(qual)
        
       
     
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
        #myLabel=tk.Label(window,text="Hola")
        #myLabel=tk.Label(window,text=city)
        
        myLabel.grid(row=1,column=0)
        #myLabel.pack()
    
    except Exception as e:
        api="Error..."

zip=tk.Entry(window)
zip.get()
#zipLabel=tk.Label(window,text=zip.get()) 
#zip.pack()

#zip=tk.Entry(window)
zip.grid(row=0,column=0)

zipButton=tk.Button(window,text="Lookup zipcode",command=ziplookup)
zipButton.grid(row=0,column=1)

window.mainloop()