# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:27:58 2020

@author: german.santos
"""
import tkinter as tk
import sqlite3 as sq3



window = tk.Tk()

window.title("Bases de datos")
window.geometry("400x600")


#Data bases

#Create a Database or connect to one
conn=sq3.connect('address_book.db')

#Create cursor

c=conn.cursor()

#Create Table

'''
c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)""")
'''
def update():
#Create a Database or connect to one
    conn=sq3.connect('address_book.db')
    c=conn.cursor()
    
    record_id=delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name=:first,
        last_name=:last,
        address=:address,
        city=:city,
        state=:state,
        zipcode=:zipcode
        
        WHERE oid=:oid
              """,
              {
                  'first':f_name_editor.get(),
                  'last':l_name_editor.get(),
                  'address':address_editor.get(),
                  'city':city_editor.get(),
                  'state':state_editor.get(),
                  'zipcode':zipcode_editor.get(),
                  'oid':record_id
                  })
    
    #Comit Changes
    conn.commit()

    #Close conection
    conn.close()
    
    editor.destroy()
    

    
# Create a function to edit record
def edit():
    global editor
    editor = tk.Tk()
    editor.title("Update A Record")
    editor.geometry("400x250")
    #Create a Database or connect to one
    conn=sq3.connect('address_book.db')

    #Create cursor

    c=conn.cursor()
    record_id=delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid ="+record_id)
    records=c.fetchall()
   
    
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
  
    
    #Create Text Boxes
    f_name_editor = tk.Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    
    l_name_editor = tk.Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20)
    
    address_editor = tk.Entry(editor,width=30)
    address_editor.grid(row=2,column=1,padx=20)
    
    city_editor = tk.Entry(editor,width=30)
    city_editor.grid(row=3,column=1,padx=20)
    
    state_editor = tk.Entry(editor,width=30)
    state_editor.grid(row=4,column=1,padx=20)
    
    zipcode_editor = tk.Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1,padx=20)
    
   
    
    #Create Text labeks
    f_name_label=tk.Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    
    l_name_label=tk.Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)
    
    address_label=tk.Label(editor,text="Address")
    address_label.grid(row=2,column=0)
                    
    city_label=tk.Label(editor,text="City")
    city_label.grid(row=3,column=0)  
    
    state_label=tk.Label(editor,text="State")
    state_label.grid(row=4,column=0)
    
    zipcode_label=tk.Label(editor,text="Zipcode")
    zipcode_label.grid(row=5,column=0)
    
 #Loop through Results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
    #Create save Buttom
    
    save_btn=tk.Button(editor,text="Save Record to database",command=update)
    
    save_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=100)
    

    #Create a Query Button
    #query_btn=tk.Button(editor,text="Show records",command=query)
    #query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)
    
    #create a delete button
    #delete_btn=tk.Button(editor,text="Delete record",command=delete)
    #delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=136)



  
    #Comit Changes
    conn.commit()

    #Close conection
    conn.close()
    
    

#Function to delete a record
def delete():
    
    
    #Create a Database or connect to one
    conn=sq3.connect('address_book.db')

    #Create cursor

    c=conn.cursor()
    
    #Insert into Table
    c.execute("DELETE FROM addresses WHERE oid="+delete_box.get())
    #Comit Changes
    conn.commit()

    #Close conection
    conn.close()

def submit():
    
    
    #Create a Database or connect to one
    conn=sq3.connect('address_book.db')

    #Create cursor

    c=conn.cursor()
    
    #Insert into Table
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'address':address.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
            })
    #Comit Changes
    conn.commit()

    #Close conection
    conn.close()
    
    #Clear the text boxes
    f_name.delete(0,tk.END)
    l_name.delete(0,tk.END)
    address.delete(0,tk.END)
    city.delete(0,tk.END)
    state.delete(0,tk.END)
    zipcode.delete(0,tk.END)
 
#Create Query function

def query():
    #Create a Database or connect to one
    conn=sq3.connect('address_book.db')

    #Create cursor

    c=conn.cursor()
    
    # Query the database
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    print(records)
    #Loop thru Results
    print_records=""
    for record in records:
        #print_records += str(record)+"\n"
        print_records += str(record[0])+" "+str(record[1])+" "+" \t"+str(record[6])+"\n"
    query_lbl=tk.Label(window,text=print_records)
    query_lbl.grid(row=12,column=0,columnspan=2)
    
    #Comit Changes
    conn.commit()

    #Close conection
    conn.close()
    return
    

#Create Text Boxes
f_name = tk.Entry(window,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name = tk.Entry(window,width=30)
l_name.grid(row=1,column=1,padx=20)

address = tk.Entry(window,width=30)
address.grid(row=2,column=1,padx=20)

city = tk.Entry(window,width=30)
city.grid(row=3,column=1,padx=20)

state = tk.Entry(window,width=30)
state.grid(row=4,column=1,padx=20)

zipcode = tk.Entry(window,width=30)
zipcode.grid(row=5,column=1,padx=20)

delete_box=tk.Entry(window,width=30)
delete_box.grid(row=9,column=1)

#Create Text labeks
f_name_label=tk.Label(window,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=tk.Label(window,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=tk.Label(window,text="Address")
address_label.grid(row=2,column=0)
                
city_label=tk.Label(window,text="City")
city_label.grid(row=3,column=0)  

state_label=tk.Label(window,text="State")
state_label.grid(row=4,column=0)

zipcode_label=tk.Label(window,text="Zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=tk.Label(window,text="Select ID ")
delete_box_label.grid(row=9,column=0,pady=5)
#Create Summut Buttom

submit_btn=tk.Button(window,text="Add Record to database",command=submit)

submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=100)

#Create a Query Button
query_btn=tk.Button(window,text="Show records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#create a delete button
delete_btn=tk.Button(window,text="Delete record",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=136)


#create a Update button
edit_btn=tk.Button(window,text="Edit record",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=143)

#Comit Changes
conn.commit()

#Close conection
conn.close()


#window.destroy()


window.mainloop()