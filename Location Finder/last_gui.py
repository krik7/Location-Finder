#grid layout
#import tkinter
from tkinter import *
from tkinter import messagebox
import os
import subprocess
def Coressoption():
    
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
root = Tk() # create root window
root.title("Frame Example")
root.iconbitmap('icon.ico')
root.config(bg="red3")
root.protocol("WM_DELETE_WINDOW", Coressoption)




















# layout mangement
#1.pack
#2.place
#3.grid


val=""
def fileputtingdata():
    ob=open("previous.data","a")
    dataforfile=input1.get()
    ob.write(dataforfile+"\n")
    
    

def LOAD():
    subprocess.call(["python", "geoload.py"])
def DUMP():
    subprocess.call(["python", "geodump.py"])
    

def Map():
    
    os.system('where.html')



    
def delete():
 
    

    if(len(input1.get()))<1:
          msg = messagebox.showwarning( "warning","Already Empty")
    else:
        val=input1.get()
        input1.delete("0",END)
          
          
           
          

    

def cleanfile():
    os.remove("previous.data")
    os.remove("geodata.sqlite")
    os.remove("where.js")
    
    


    

    
root.title("Smart location Finder")
root.geometry('600x620')
root.resizable(False, False)
k=PhotoImage(file="logo-removebg-preview.png" )
#bg='black'
Label(root,image=k,fg='black',bg='black').pack(pady=10)
root.configure(background="Black")
l1=Label(root,text="Let's Get Started",fg="#D95406",bg="black",font=("verdana",18))
l1.pack()
input1=Entry(root,text="",font=("verdana",20),relief=FLAT)
input1.pack(side=TOP,padx=10,pady=55)
B=Button(root,text="Submit",activebackground="white",fg='white',bg="#0365A6" ,font=("verdana",12),relief=FLAT,command= fileputtingdata)
B.pack(ipadx=2)
B=Button(root,text="LOAD ",activebackground="white",fg='white',bg="#0365A6" ,font=("verdana",12),relief=FLAT,command= LOAD)
B.pack(pady=12 ,ipadx=6)
B=Button(root,text="Execute",activebackground="white",fg='white',bg="#0365A6" ,font=("verdana",12),relief=FLAT,command= DUMP)
B.pack(pady=4)
b6=Button(root,text="Clear",fg='white',bg="#0365A6"  ,activeforeground="grey",font=("verdana",12) ,relief=FLAT,command= delete)
b6.pack(pady=10,ipadx=11)
b6=Button(root,text="Map",fg='white',bg="#0365A6"  ,activeforeground="grey",font=("verdana",12) ,relief=FLAT,command= Map)
b6.pack(ipadx=16,padx=3,pady=5)
b7=Button(root,text="Clean",fg='white',bg="#0365A6"  ,activeforeground="grey",font=("verdana",12) ,relief=FLAT,command= cleanfile)
b7.pack(ipadx=10,pady=8)
root.mainloop()
#input1.pack(fill='both')
#create text field

