import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
from logs import logs
from currency_transfer import currency_trans
from money import open_account, withdraw_usd, usd_deposit, currency_transfer, cur_check

class currency(tk.Toplevel):    
    def __init__(self, master, nick, balance=0):
        self.nick = nick
        self.balance = balance
        self.path_customers = 'customers\\'
        self.path_logs = "logs\\"
        self.log = logs()
        tk.Toplevel.__init__(self, master)
        tk.Tk.configure(self, bg="white")
        tk.Tk.geometry(self, "400x400")
        tk.Tk.title(self, "Currency Menu")
        global check
        self.depo = tk.IntVar()
        self.check = tk.StringVar(self,"Currency control menu")
        tk.Label(self, textvariable=self.check, fg="green", font = ("Algerian", 13)).pack() 
        tk.Label(self, text="").pack()                                                              ######
        tk.Label(self, text="Check your current ballance").pack()                           ########          MAIN BODY WITH BUTTONS/ENTRIES ETC.
        tk.Button(self, text="Check", bg="green", command=self.status).pack()
        tk.Label(self, text="").pack()
        self.depo2_entry = tk.Entry(self, bg="yellow")
        self.depo2_entry.pack()
        tk.Button(self, text="Deposit", bg="green", command=self.deposit_usd).pack()
        tk.Label(self, text="").pack()
        self.with_entry = tk.Entry(self, bg="yellow")
        self.with_entry.pack()
        tk.Button(self, text="Withdraw", bg="green", command=self.withdraw_usd).pack()
        tk.Button(self, text="Transfer", bg="green", command=self.trans_menu).pack()

    def trans_menu(self):           ### Recalls new window for currency transfers
        self.screen = tk.Toplevel(self)
        self.screen.geometry("350x200")
        self.screen.title("transfers")
        tk.Label(self.screen, text = "Do you transfers", bg="blue", font = ("Algerian", 13)).pack()
        tk.Label(self.screen, text="").pack()
        global login
        global amount
        self.login = tk.Entry(self.screen, bg="yellow")
        self.login.insert(0, "Put user here")
        self.login.pack()
        tk.Label(self, text="").pack()
        self.amount = tk.Entry(self.screen, bg="yellow")
        self.amount.insert(0, "Put money amount here")
        self.amount.pack()
        tk.Button(self.screen, text="transfer", bg="green", command=self.systems).pack()

    def systems(self):         
        self.login_load = self.login.get()
        self.amount_load = float(self.amount.get())
        
        currency_transfer(self.login_load, self.nick, self.amount_load)
        
        var = ('%s' % float(self.amount_load)) #<---- Transform decimal value to string to be displayable
        messagebox.showinfo("success", "You have transfered: "+var+" usd")
        self.log.transfer_usd_logs(self.nick, self.login_load, self.amount_load)
            
    
    def status(self): ###### current balance of currency accoount
        cur_check(self.nick)

    def deposit_usd(self):
        self.usd = float(self.depo2_entry.get()) 
        self.balance = float(self.balance)

        if not self.usd:
            messagebox.showerror('error','empty field')
        elif self.usd < 0:
            messagebox.showerror('error','cannot deposit negative amount')
        else:
            usd_deposit(self.usd,self.nick)
            messagebox.showinfo('info',"you have deposited: "+str(self.usd)+"$")
            self.log.depo_usd_logs(self.nick, self.usd)

    def withdraw_usd(self):
        self.balance = float(self.balance)
        self.usd = float(self.with_entry.get()) 
        if not self.usd:
            messagebox.showerror('error','empty field')
        elif self.usd < 0:
            messagebox.showerror('error','cannot withdraw negative amount')
        else:
            withdraw_usd(self.usd, self.nick)
            messagebox.showinfo('info',"you have withdrawed: "+str(self.usd)+"$")
            self.log.with_usd_logs(self.nick, self.usd)


class currency_new(tk.Toplevel):
    def __init__(self, master, nick, kill):
        self.kill = kill
        self.nick = nick
        self.path_customers = "customers\\"
        self.log = logs()
        tk.Toplevel.__init__(self, master)
        tk.Tk.configure(self, bg="white")
        tk.Tk.geometry(self, "300x250")
        tk.Tk.title(self, "Currency account creation")
        tk.Label(self, text = "Currency menu", bg="blue", font = ("Algerian", 13)).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Create", bg="green", command=self.create).pack()
        tk.Label(self, text="").pack()

    def create(self):
        open_account(self.nick)
        tk.Label(self, text="Currency account opened", fg="green", font=("calibri", 11)).pack()
        tk.Label(self.kill, text='').pack()
        tk.Button(self.kill, text="Add funds to currency", bg="red", command=lambda:currency_trans(self, self.nick)).pack()
        self.log.currency_logs_on(self.nick)
        self.withdraw()

