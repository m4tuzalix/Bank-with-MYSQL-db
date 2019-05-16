import tkinter as tk 
import math
from tkinter import messagebox
from money import pln_to_currency
import sqlite3

class currency_trans(tk.Toplevel):
    def __init__(self, master, name):
        self.name=name
        self.path_customers = "customers\\"
        tk.Toplevel.__init__(self, master)
        global file
        with open(self.path_customers+self.name, 'r') as file:
            lines=file.readlines()
        self.title("Add funds to currency")
        self.geometry("350x250")
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.name,))
        for row in cur.fetchall():
            self.nazwa = str(row[4])
        self.balance = tk.StringVar(self, "Available balance: "+self.nazwa)
        self.info = tk.Label(self, textvariable=self.balance, fg="green", font = ("Algerian", 13))
        self.info.pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        self.funds = tk.Entry(self)
        self.funds.pack()
        tk.Button(self, text="proceed", command=self.mechanism).pack()
        self.info2 = tk.StringVar(self)
        tk.Label(self, textvariable=self.info2, fg="green").pack()

    def mechanism(self):
        self.amount = float(self.funds.get())
        if self.amount < 0:
            messagebox.showerror('error', 'cannot proceed negative amount')
        else:
            pln_to_currency(self.amount,self.name)
            con = sqlite3.connect('databases\\main.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM users WHERE login=?',(self.name,))
            for row in cur.fetchall(): 
                self.balance.set('%s' % (str(row[4]))) #/////// shows row[4] value as the balance
                if row[4]>self.amount:
                    self.info2.set("Succes, "+'%s' % (round(self.amount/3.70, 2))+" usd added")
                else:
                    self.info2.set('')
            con.commit()
            con.close()
        
                
                
            
            

    
        
        
