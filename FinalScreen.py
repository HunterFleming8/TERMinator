from numpy import *
import tkinter
from tkinter import *
import PIL

fs=Tk()
fs.title('Begin')
fs.geometry('1218x684')
fs.configure(bg='#afffff')

def restartscreen():
   fs.destroy()
   import InitialScreen

def startIK():
   fs.destroy()
   import InverseKinematics

#Cancel Button
cnl_frame=Frame(fs,bd=0)
cnl_frame.place(x=700,y=460)
cnl_button=Button(cnl_frame,fg="#f0003c",highlightbackground='#f0003c',highlightthickness=3, text="CANCEL",relief=RAISED,font=('Andale Mono',40),command=restartscreen)
cnl_button.pack()

#Begin Button
begin_frame=Frame(fs,highlightbackground='#0ce696')
begin_frame.place(x=400,y=460)
begin_button=Button(begin_frame,fg='#0ce696',highlightbackground='#0ce696',highlightthickness=3,text="BEGIN",relief=RAISED,font=('Andale Mono',40),command=startIK)
begin_button.pack()

label_y=Label(fs,text="Ready to Begin?",font=('Andale Mono',70),bg='#9DA6D3')
label_y.place(x=320,y=230)

close_frame=Frame(fs,bd=0)
close_frame.place(x=1150,y=10)
close_btn=Button(close_frame,text="✖️",font=('Andale Mono',15),command=fs.destroy)
close_btn.pack()

fs.mainloop()