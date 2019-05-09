import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
from logs import logs
from money import send_cash

class trans(tk.Toplevel):
    def __init__(self, master, nick):
        self.nick = nick
        self.path_customers = "C:\\Users\\Mateusz\\Desktop\\bank project\\customers\\"
        self.path_logs = "C:\\Users\\Mateusz\\Desktop\\bank project\\logs\\"
        self.logs = logs()
        tk.Toplevel.__init__(self, master)
        tk.Tk.configure(self, bg="white")
        tk.Tk.geometry(self, "300x250")
        tk.Tk.title(self, "Transfer Menu")
        tk.Label(self, text = "DO you transfers", bg="blue", font = ("Algerian", 13)).pack()
        tk.Label(self, text="").pack()
        global tescik
        global tescik2
        self.tescik = tk.Entry(self, bg="yellow")
        self.tescik.insert(0, "Put user here")
        self.tescik.pack()
        tk.Label(self, text="").pack()
        self.tescik2 = tk.Entry(self, bg="yellow")
        self.tescik2.insert(0, "Put amount here")
        self.tescik2.pack()
        tk.Button(self, text="transfer", bg="green", command=self.send).pack()

    def send(self):  
        self.login_load = self.tescik.get()
        self.amount_load = float(self.tescik2.get())
        if self.amount_load < 0:
            messagebox.showerror('error', 'Cannot transfer negative amount')
        elif not self.amount_load:
            messagebox.showerror('error','Empty field')
        else:
            send_cash(self.amount_load,self.nick, self.login_load) #/// calls function in database
            messagebox.showinfo('info','You have sent: '+str(self.amount_load+' to: '+str(self.login_load)))
            

