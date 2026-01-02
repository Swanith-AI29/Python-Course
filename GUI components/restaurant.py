import tkinter as tk 
from tkinter import ttk,messagebox
class Restaurantordermanagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant management app")
        self.menu_items={"French Fries":2,"Lunch meal":2,"Burger meal":3,"pizza meal":4,"Cheese burger":2.5,"Drinks":1}
        self.exchange_rate=82
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Restaurant order management",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels={}
        self.menu_quantities={}
        for i,(item,price)in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item}(${price}):",font=("Arial",12))
            label.grid(row=i,padx=10,pady=5)
            self.menu_labels[item]=label
            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=1,column=1,padx=18,pady=5)
            self.menu_quantities[item]=quantity_entry
        self.currency_var=tk.StringVar()
        ttk.Label(frame,text="Currency:",font=("Arial",12)).grid(row=len(self.menu_items)+1,column=8,padx=18,pady=5)
        currency_dropdown=ttk.Combobox(frame,textvariable=self.currency_var,state="readonly",width=18,values=('USD','INR'))
        currency_dropdown.grid(row=len(self.menu_items)+1,
        column=1,padx=10,pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace('w',self.update_menu_prices)
