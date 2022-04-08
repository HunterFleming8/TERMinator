from tkinter import messagebox
from numpy import *
from tkinter import *

ps=Tk()
ps.title('Positioning')
ps.geometry('1218x684')
ps.configure(bg='#afffff')

def previousPageEF():
    ps.destroy()
    import ChooseEndEffectorScreen


label_q=Label(ps,text="Input Desired Positioning",font=('Andale Mono',55),bg='#afffff',fg='black')
label_q.place(x=230,y=100)

xcoord_label=Label(ps,text="X-Coordinate",font=("Andale Mono",15),bg="#7F7DFB",fg='white')
ycoord_label=Label(ps,text="Y-Coordinate",font=("Andale Mono",15),bg="#7F7DFB",fg='white')
zcoord_label=Label(ps,text="Z-Coordinate",font=("Andale Mono",15),bg="#7F7DFB",fg='white')

var1=IntVar()
var2=IntVar()
var3=IntVar()

xcoord_entry=Entry(ps,textvariable=var1,font=("Andale Mono",15),bg="#b7d1ff",fg="#7F7DFB")
ycoord_entry=Entry(ps,textvariable=var2,font=("Andale Mono",15),bg="#b7d1ff",fg="#7F7DFB")
zcoord_entry=Entry(ps,textvariable=var3,font=("Andale Mono",15),bg="#b7d1ff",fg="#7F7DFB")

xcoord=xcoord_entry.get()
ycoord=ycoord_entry.get()
zcoord=zcoord_entry.get()

def nextPageLS():
    global xcoord
    global ycoord
    global zcoord
    xcoord=float(xcoord_entry.get())
    ycoord=float(ycoord_entry.get())
    zcoord=float(zcoord_entry.get())
    ps.destroy()
    import LengthScreen

def CoordinateEntries():
    xcoord=xcoord_entry.get()
    ycoord=ycoord_entry.get()
    zcoord=zcoord_entry.get()
    confirm=messagebox.askokcancel('Confirm Coordinates',f'You entered:\nX-Coordinate = {xcoord}\nY-Coordinate = {ycoord}\nZ-Coordinate = {zcoord}')
    if confirm==True:
       command=nextPageLS()
    if confirm==False:
        messagebox.showinfo('Cancel',"Input Coordinates Again!")



xcoord_label.place(x=500,y=253)
xcoord_entry.place(x=650,y=250)
ycoord_label.place(x=500,y=353)
ycoord_entry.place(x=650,y=350)
zcoord_label.place(x=500,y=453)
zcoord_entry.place(x=650,y=450)

ent_frame=Frame(ps,bd=0)
ent_frame.place(x=600,y=550)
ent_btnn=Button(ent_frame,text="ENTER",font=("Andale Mono",33),command=CoordinateEntries,highlightthickness=3,highlightbackground='#5900ee',fg='#5900ee')
ent_btnn.pack()


rtn_frame=Frame(ps,bd=0)
rtn_frame.place(x=10,y=620)
rtn_btn=Button(rtn_frame,text='⬅',font=('Andale Mono',33),command=previousPageEF)
rtn_btn.pack()

close_frame=Frame(ps,bd=0)
close_frame.place(x=1150,y=10)
close_btn=Button(close_frame,text="✖️",font=('Andale Mono',15),command=ps.destroy)
close_btn.pack()

ps.mainloop()
