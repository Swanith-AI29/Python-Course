from tkinter import*
from tkinter import messagebox
widget=Tk()
widget.title("Calculator")
widget.geometry("600x550")
widget.configure(bg="black")
headinglabel=Label(text="Calculator2000",height=4,width=20)
headinglabel.place(x=289,y=1)
def oneclick():
    messagebox.showinfo("Alert","button 1 is pressed")
a=Button(text="1",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=oneclick)
a.place(x=1,y=1)
def twoclick():
    messagebox.showinfo("Alert","button 2 is pressed")
b=Button(text="2",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=twoclick)
b.place(x=108,y=1)
def threeclick():
    messagebox.showinfo("Alert","button 3 is pressed")
c=Button(text="3",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=threeclick)
c.place(x=215,y=1)
def fourclick():
    messagebox.showinfo("Alert","button 4 is pressed")
d=Button(text="4",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=fourclick)
d.place(x=1,y=85)
def fiveclick():
    messagebox.showinfo("Alert","button 5 is pressed")
e=Button(text="5",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=fiveclick)
e.place(x=108,y=85)
def sixclick():
    messagebox.showinfo("Alert","button 6 is pressed")
d=Button(text="6",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=sixclick)
d.place(x=215,y=85)
g=Button(text="7",fg="White",bg="grey",height=5,width=10)
g.place(x=1,y=323)
h=Button(text="8",fg="White",bg="grey",height=5,width=10)
h.place(x=151,y=323)
i=Button(text="9",fg="White",bg="grey",height=5,width=10)
i.place(x=301,y=323)
j=Button(text="0",fg="White",bg="grey",height=5,width=10)
j.place(x=1,y=484)
k=Button(text="=",fg="White",bg="grey",height=5,width=21)
k.place(x=151,y=484)
l=Button(text="/",fg="White",bg="grey",height=5,width=10)
l.place(x=449,y=484)
m=Button(text="*",fg="White",bg="grey",height=5,width=10)
m.place(x=451,y=323)
n=Button(text="-",fg="White",bg="grey",height=5,width=10)
n.place(x=451,y=162)

o=Button(text="+",fg="White",bg="grey",height=5,width=10)
o.place(x=451,y=1)
widget.mainloop()
height=5,width