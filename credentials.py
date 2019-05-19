import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
from banking import bank
import time
import sqlite3



class back(tk.Toplevel):
    def __init__(self, master, but, counter=3):
        self.but = but
        self.but.configure(state=tk.DISABLED)
        tk.Toplevel.__init__(self, master)
        self.counter = counter
        self.info = tk.StringVar()
        self.info2 = tk.StringVar()
        self.info3 = tk.StringVar()
        self.path_logs = "logs\\"
        self.geometry("350x200")
        self.title("smiglo")
        tk.Label(self, text="Put your login").pack()
        tk.Label(self, text="").pack()
        tk.Entry(self, textvariable=self.info, bg="yellow").pack()
        tk.Button(self, text="Check", bg="green", command=self.password).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, textvariable=self.info2).pack()
        tk.Label(self, textvariable=self.info3).pack()
        tk.Tk.protocol(self, 'WM_DELETE_WINDOW', lambda:self.close(self.but, self))
        
    def close(self, buto, wind):
        self.buto = buto
        self.wind = wind
        self.buto.configure(state=tk.ACTIVE)
        self.wind.destroy()
        
    def password(self):
        global get
        global lines 
        global file 
        global entry
        global answer
        global final
        self.final = tk.StringVar()
        self.answer = tk.StringVar()
        self.get = self.info.get() 
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Check", command=self.valid)
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.get,))
        if cur.fetchone():
            self.geometry("500x400")
            self.info2.set("Answer to your secret question:")
            cur.execute('SELECT * FROM users WHERE login=?',(self.get,))
            for row in cur.fetchall():
                self.info3.set(row[6])
            self.entry.pack()
            self.button.pack()
            tk.Label(self, textvariable=self.final).pack()
        else:
            messagebox.showerror('error', 'user cannot be identified')
            self.geometry("350x200")
            self.info3.set("")
            self.info2.set("")
            self.entry.destroy()
            self.button.destroy()

    def valid(self):
        self.counter = self.counter
        self.check = self.entry.get()
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.get,))
        for row in cur.fetchall():
            if row[7] == self.check:
                self.but.configure(state=tk.ACTIVE)
                messagebox.showinfo("succes","Your password: "+str(row[2]))
                self.destroy()
        else:
            self.counter = self.counter - 1
            self.lol = messagebox.showwarning("warning", "wrong password!! more attempts: "+str(self.counter))
            if self.counter == 0:
                messagebox.showinfo("Bye", "Program will close within 5 seconds")
                for x in range(5, -1, -1):
                    time.sleep(1)
                    if x==0:
                        exit()

        
            
                
            



            