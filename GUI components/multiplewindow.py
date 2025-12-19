from tkinter import*
window=Tk()
window.title("topwindow")
window.geometry("550x600")
rootlabel=Label(text="This is root level",height=3,width=25,font=("Courier",19))
rootlabel.pack()

window2=Toplevel()
window2.title("toplevelwindow")
window2.geometry("200x300")
toplevellabel=Label(window2,text="This is a top level window",height=3,width=25,font=("Courier",15))
toplevellabel.pack()
window.mainloop()
