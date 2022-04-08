#Initial Screen
import numpy
from tkinter import *
from turtle import bgcolor
ws=Tk()
ws.title('TERMinator')
ws.geometry('1218x684')
ws.configure(bg='#afffff')

def nextPageEF():
   ws.destroy()
   import ChooseEndEffectorScreen


label1=Label(ws,text="Welcome to TERMinator!\nDo you wish to proceed?",font=('Andale Mono',56),bg='#9DA6D3')
label1.place(x=220,y=230)

proc_frame=Frame(ws,bg='#BCA7F8',bd=3)
proc_frame.place(x=500,y=500)
proc_btn=Button(proc_frame,text="PROCEED",fg='#BCA7F8',relief=RAISED,font=('Andale Mono',40),command=nextPageEF)
proc_btn.pack()

close_frame=Frame(ws,bd=0)
close_frame.place(x=1150,y=10)
close_btn=Button(close_frame,text="✖️",font=('Andale Mono',15),command=ws.destroy)
close_btn.pack()

ws.mainloop()





