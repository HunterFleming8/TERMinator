#Choose End Effector Screen

from tkinter import *
from tkinter import messagebox
from numpy import *

def previousPageIS():
    ef.destroy()
    import InitialScreen

def nextPagePS():
    ef.destroy()
    import PositioningScreen

ef=Tk()
ef.title('End Effector Choice')
ef.geometry("1218x684")
ef.configure(bg='#afffff')

label_a=Label(ef,text="Choose End Effector",font=('Andale Mono',55),bg='#6ed7d7')
label_a.place(x=340,y=110)

def EndChoice():
    choice=var.get()
    if choice==1:
        output="Blaster"
    if choice==2:
        output="Other"
    confirm=messagebox.askokcancel('Confirm End Effector Choice',f'Confirm End Effector Choice!\nYou Have Chosen: {choice}')
    if confirm==True:
        command=nextPagePS()
    if confirm==False:
      messagebox.showinfo('Cancel',"Choose End Effector Again!")

var=StringVar()
blasterchoice=Radiobutton(ef,text="Blaster",font=("Andale Mono",33),bg="#e7ddff",variable=var,value="Blaster",command=EndChoice)
blasterchoice.place(x=570,y=250)
otherchoice=Radiobutton(ef,text="Other",font=("Andale Mono",33),bg="#e7ddff",command=EndChoice,variable=var,value='Other')
otherchoice.place(x=570,y=350)

ent_frame=Frame(ef,bd=0)
ent_frame.place(x=570,y=470)
ent_btnn=Button(ent_frame,text="ENTER",font=("Andale Mono",33),command=EndChoice,highlightthickness=3,
highlightbackground='#5900ee',fg='#5900ee')
ent_btnn.pack()

rtn_frame=Frame(ef,bd=0)
rtn_frame.place(x=10,y=620)
rtn_btn=Button(rtn_frame,text='⬅',font=('Andale Mono',33),command=previousPageIS)
rtn_btn.pack()

close_frame=Frame(ef,bd=0)
close_frame.place(x=1150,y=10)
close_btn=Button(close_frame,text="✖️",font=('Andale Mono',15),command=ef.destroy)
close_btn.pack()

ef.mainloop()



