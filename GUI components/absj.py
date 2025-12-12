from tkinter import*
from tkinter import messagebox

widget=Tk()
widget.title("Calculator")
widget.geometry("600x550")
widget.configure(bg="black")

expression=""

def update(val):
    global expression
    expression+=str(val)
    display.config(text=expression)

def calculate():
    global expression
    try:
        result=str(eval(expression))
        display.config(text=result)
        expression=result
    except:
        display.config(text="Error")
        expression=""

def clear():
    global expression
    expression=""
    display.config(text="")

display=Label(text="",height=2,width=25,bg="white",font=("Courier",20))
display.place(x=120,y=20)

def oneclick():
    update(1)
a=Button(text="1",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=oneclick)
a.place(x=40,y=100)

def twoclick():
    update(2)
b=Button(text="2",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=twoclick)
b.place(x=160,y=100)

def threeclick():
    update(3)
c=Button(text="3",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=threeclick)
c.place(x=280,y=100)

def plusclick():
    update("+")
o=Button(text="+",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=plusclick)
o.place(x=400,y=100)

def fourclick():
    update(4)
d=Button(text="4",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=fourclick)
d.place(x=40,y=190)

def fiveclick():
    update(5)
e=Button(text="5",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=fiveclick)
e.place(x=160,y=190)

def sixclick():
    update(6)
f=Button(text="6",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=sixclick)
f.place(x=280,y=190)

def minusclick():
    update("-")
n=Button(text="-",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=minusclick)
n.place(x=400,y=190)

def sevenclick():
    update(7)
g=Button(text="7",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=sevenclick)
g.place(x=40,y=280)

def eightclick():
    update(8)
h=Button(text="8",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=eightclick)
h.place(x=160,y=280)

def nineclick():
    update(9)
i=Button(text="9",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=nineclick)
i.place(x=280,y=280)

def multiplyclick():
    update("*")
m=Button(text="*",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=multiplyclick)
m.place(x=400,y=280)

def zeroclick():
    update(0)
j=Button(text="0",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=zeroclick)
j.place(x=40,y=370)

def equalclick():
    calculate()
k=Button(text="=",fg="White",bg="grey",height=3,width=18,font=("Courier",15),command=equalclick)
k.place(x=160,y=370)

def divideclick():
    update("/")
l=Button(text="/",fg="White",bg="grey",height=3,width=8,font=("Courier",15),command=divideclick)
l.place(x=400,y=370)

clearbtn=Button(text="C",fg="White",bg="red",height=3,width=8,font=("Courier",15),command=clear)
clearbtn.place(x=40,y=450)

widget.mainloop()
