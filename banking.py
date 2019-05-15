import tkinter as tk
import os
import sqlite3
import random
from tkinter import messagebox
from tkinter import font as tkfont
import string
from transfers import trans
from currency import currency, currency_new
from logs import logs
from currency_transfer import currency_trans
from admin import admin_chat
from hazard import roulete, lotto, lotto_los
from money import deposit_cash, withdraw_cash, cash_check, status, Token_open, Token_close, Account_type
from gui import gui
from usergui import gui2





class bank(tk.Tk):

    def __init__(self, name, password, code, balance=0): ## Script opens for person who provide login/password/security code

        self.balance = balance
        self.name = name
        self.password = password
        self.code = code
        self.log = logs()
        self.path_customers = "customers\\"
        self.path_logs = "logs\\"



        tk.Tk.__init__(self)
        status(self.name) #///// sets user's status to ONLINE
        
        tk.Tk.title(self, "Smiglo bank "+'logged as: '+str(self.name))
        tk.Tk.geometry(self,"400x500")
        tk.Tk.protocol(self,'WM_DELETE_WINDOW', self.x_disable)
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="deposit", bg="red", command=self.deposit).pack()    ##### Main Body
        self.depo_entry = tk.Entry(self, bg="yellow")
        self.depo_entry.pack()
        tk.Button(self, text="withdraw", bg="red", command=self.withdraw).pack()
        self.withh_entry = tk.Entry(self, bg="yellow")
        self.withh_entry.pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Check balance", bg="red", command=self.check).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Log Off", bg="pink", command=self.log_off).pack(side=tk.BOTTOM)
        tk.Tk.after(self, 100, self.currency_check)
        tk.Tk.after(self, 100, self.token_check)

    # Submenus
        menu = tk.Menu(self)
        tk.Tk.config(self, menu=menu)

        Sub = tk.Menu(menu)
        menu.add_cascade(label="transfers", menu=Sub) ##////////    Submenu for transfers
        Sub.add_command(label="Do transfer", command=lambda: trans(self, self.name))

        Sub2 = tk.Menu(menu)
        menu.add_cascade(label="Currency", menu=Sub2)     #//////// SuBmenu for currency
        Sub2.add_command(label="Currency manu", command=self.currency)

        Sub3 = tk.Menu(menu)
        menu.add_cascade(label="Admin chat", menu=Sub3)
        Sub3.add_command(label="Open admin chat", command=lambda: admin_chat(self, self.name, self.password, self.code)) #////// admin chat (currently only shows if admin ONLINE)

        Sub4 = tk.Menu(menu)
        menu.add_cascade(label="Roulete", menu=Sub4)
        Sub4.add_command(label="Play roulete", command=lambda: roulete(self, self.name)) #////// roulete game

        Sub5 = tk.Menu(menu)
        menu.add_cascade(label="Lotto", menu=Sub5)
        Sub5.add_command(label="Play lotto", command=lambda: lotto_los(self, self.name)) #////// lotto game

        Sub6 = tk.Menu(menu)
        menu.add_cascade(label="shop", menu=Sub6)
        Sub6.add_command(label="Play lotto", command=self.Go_to_shop)
    
    
    def Go_to_shop(self):
        for rows in Account_type(self.name):
            if rows[10]=="ADMIN":
                gui(self,self.name)
            else:
                gui2(self,self.name)


    def log_off(self):
        self.log.log_on(self.name) 
        status(self.name) #////// OFFLINE status
        self.destroy()
        
    def currency_check(self):
        con = sqlite3.connect('databases\\users.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE login=?",(self.name,))
        rows = cur.fetchall()
        for row in rows:
            if row[5] != 'Not opened':
                tk.Button(self, text="Add funds to currency", bg="red", command=lambda: currency_trans(self, self.name)).pack()
                tk.Label(self, text="").pack()
            else:
                pass      
        con.commit()
        con.close()
                
            

    def x_disable(self):
        pass

    def token_check(self):
        con = sqlite3.connect('databases\\users.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE login=?",(self.name,))
        rows = cur.fetchall()
        for row in rows:
            if row[8] == 'No token':
                global button
                self.button = tk.Button(self, text="Activate_token", bg="red", command=self.activation)
                self.button.pack()
            else:
                global button2
                self.button2 = tk.Button(self, text="Deactivation", bg="red", command=self.deactiv)
                self.button2.pack()
    
    def activation(self):
        self.button.destroy()
        self.button2 = tk.Button(self, text="Deactivation", bg="red", command=self.deactiv)
        self.button2.pack()
        Token_open(self.name)
        self.log.token_logs_on(self.name)

    def deactiv(self):
        self.button2.destroy()
        self.button = tk.Button(self, text="Activate_token", bg="red", command=self.activation)
        self.button.pack()
        Token_close(self.name)
        self.log.token_logs_off(self.name)



    def currency(self):
        con = sqlite3.connect('databases\\users.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE login=?",(self.name,))
        rows = cur.fetchall()
        for row in rows:
            if row[5] == 'Not opened':
                currency_new(self,self.name,self)
            else:
                currency(self,self.name)
            

    def transfer(self): ### Opens menu transfers
        trans(self, self.name)

    def check(self): ### Allows to check the current ballance basing on the line where it is saved in file
        cash_check(self.name)
    
    def deposit(self): ### Allows to add funds to account
            self.amt = float(self.depo_entry.get())
            if not self.amt:
                messagebox.showerror('error','empty field')
            elif self.amt < 0:
                messagebox.showerror('error','cannot deposit negative amount')
            else:
                deposit_cash(self.amt,self.name)
                messagebox.showinfo('info',"you have deposited: "+str(self.amt))
                self.depo_entry.delete(0, tk.END)
                self.log.depo_logs(self.name, self.amt)
        
                 
    def withdraw(self): 
        self.amt2 = float(self.withh_entry.get())
        if not self.amt2:
            messagebox.showerror('error','empty field')
        elif self.amt2 < 0:
            messagebox.showerror('error','cannot withdraw negative amount')
        else:
            withdraw_cash(self.amt2,self.name)
            messagebox.showinfo('info',"you have withdrawed: "+str(self.amt2))
            self.withh_entry.delete(0, tk.END)
            self.log.with_logs(self.name, self.amt2)