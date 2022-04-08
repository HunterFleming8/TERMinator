from tkinter import messagebox
from numpy import *
from tkinter import *

ls=Tk()
ls.title('Lengths of Joints')
ls.geometry('1218x684')
ls.configure(bg='#afffff')

def previousPagePS():
    ls.destroy()
    import PositioningScreen

    

label_j=Label(ls,text="Input Length of Joints",font=('Andale Mono',55),bg='#afffff',fg='black')
label_j.place(x=300,y=100)

baseHeight_label=Label(ls,text="Base Height",font=("Andale Mono",15,),bg="#82c4d8",fg='white')
upperArm_label=Label(ls,text="UpperArm Length",font=("Andale Mono",15),bg="#82c4d8",fg='white')
foreArm_label=Label(ls,text="Forearm Length",font=("Andale Mono",15),bg="#82c4d8",fg='white')

baseHeightunit_label=Label(ls,text="cm",font=('Andale Mono',15),fg='black',bg='#afffff')
upperArmunit_label=Label(ls,text="cm",font=('Andale Mono',15),fg='black',bg='#afffff')
foreArmunit_label=Label(ls,text="cm",font=('Andale Mono',15),fg='black',bg='#afffff')

var4=IntVar()
var5=IntVar()
var6=IntVar()

baseHeight_entry=Entry(ls,textvariable=var4,font=("Andale Mono",15),bg="#b7d1ff",fg="white")
upperArm_entry=Entry(ls,textvariable=var5,font=("Andale Mono",15),bg="#b7d1ff",fg="white")
foreArm_entry=Entry(ls,textvariable=var6,font=("Andale Mono",15),bg="#b7d1ff",fg="white")

baseHeight=baseHeight_entry.get()
upperArm=upperArm_entry.get()
foreArm=foreArm_entry.get()

def nextPageFS():
    global baseHeight
    global upperArm
    global foreArm
    baseHeight=float(baseHeight_entry.get())
    upperArm=float(upperArm_entry.get())
    foreArm=float(foreArm_entry.get())
    ls.destroy()
    import FinalScreen

def JointEntries():
    baseHeight=baseHeight_entry.get()
    upperArm=upperArm_entry.get()
    foreArm=foreArm_entry.get()
    confirm=messagebox.askokcancel('Confirm Joint Lengths',f'You entered:\nbaseHeight= {baseHeight}\nupperArm = {upperArm}\nforeArm = {foreArm}')
    if confirm==True:
       command=nextPageFS()
    if confirm==False:
        messagebox.showinfo('Cancel',"Input Joints Again!")


baseHeight_label.place(x=500,y=252)
baseHeight_entry.place(x=650,y=250)
baseHeightunit_label.place(x=850,y=252)
upperArm_label.place(x=500,y=352)
upperArm_entry.place(x=650,y=350)
upperArmunit_label.place(x=850,y=352)
foreArm_label.place(x=500,y=452)
foreArm_entry.place(x=650,y=450)
foreArmunit_label.place(x=850,y=452)

ent_frame=Frame(ls,bd=0)
ent_frame.place(x=600,y=580)
ent_btnn=Button(ent_frame,text="ENTER",font=("Andale Mono",33),command=JointEntries,highlightthickness=3,highlightbackground='#5900ee',fg='#5900ee')
ent_btnn.pack()

rtn_frame=Frame(ls,bd=0)
rtn_frame.place(x=10,y=620)
rtn_btn=Button(rtn_frame,text='⬅',font=('Andale Mono',33),command=previousPagePS)
rtn_btn.pack()

close_frame=Frame(ls,bd=0)
close_frame.place(x=1150,y=10)
close_btn=Button(close_frame,text="✖️",font=('Andale Mono',15),command=ls.destroy)
close_btn.pack()

ls.mainloop()



