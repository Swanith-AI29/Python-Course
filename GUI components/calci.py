from tkinter import*
from tkinter import messagebox
widget=Tk()
widget.title("Calculator")
widget.geometry("430x460")
widget.configure(bg="black")
headinglabel=Label(text="Calculator2000",height=5,width=15,font=("Courier",15))
headinglabel.place(x=155,y=1)
def oneclick():
    messagebox.showinfo("Alert","button 1 is pressed")
a=Button(text="1",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=oneclick)
a.place(x=1,y=120)
def twoclick():
    messagebox.showinfo("Alert","button 2 is pressed")
b=Button(text="2",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=twoclick)
b.place(x=108,y=120)
def threeclick():
    messagebox.showinfo("Alert","button 3 is pressed")
c=Button(text="3",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=threeclick)
c.place(x=215,y=120)
def fourclick():
    messagebox.showinfo("Alert","button 4 is pressed")
d=Button(text="4",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=fourclick)
d.place(x=1,y=204)
def fiveclick():
    messagebox.showinfo("Alert","button 5 is pressed")
e=Button(text="5",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=fiveclick)
e.place(x=108,y=204)
def sixclick():
    messagebox.showinfo("Alert","button 6 is pressed")
f=Button(text="6",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=sixclick)
f.place(x=215,y=204)
def sevenclick():
    messagebox.showinfo("Alert","button 7 is pressed")
g=Button(text="7",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=sevenclick)
g.place(x=1,y=288)
def eightclick():
    messagebox.showinfo("Alert","button 8 is pressed")
h=Button(text="8",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=eightclick)
h.place(x=108,y=288)
def nineclick():
    messagebox.showinfo("Alert","button 9 is pressed")
i=Button(text="9",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=nineclick)
i.place(x=215,y=288)
def zeroclick():
    messagebox.showinfo("Alert","button 0 is pressed")
j=Button(text="0",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=zeroclick)
j.place(x=1,y=372)
def equalclick():
    messagebox.showinfo("Alert","button = is pressed")
i=Button(text="=",fg="White",bg="grey",height=2,width=13,font=("Courier",20),command=equalclick)
i.place(x=108,y=372)
def barclick():
    messagebox.showinfo("Alert","button / is pressed")
l=Button(text="/",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=barclick)
l.place(x=323,y=372)
def starclick():
    messagebox.showinfo("Alert","button * is pressed")
m=Button(text="*",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=starclick)
m.place(x=322,y=288)
def minusclick():
    messagebox.showinfo("Alert","button - is pressed")
n=Button(text="-",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=minusclick)
n.place(x=322,y=204)

def plusclick():
    messagebox.showinfo("Alert","button + is pressed")
o=Button(text="+",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=plusclick)
o.place(x=322,y=120)
widget.mainloop()
