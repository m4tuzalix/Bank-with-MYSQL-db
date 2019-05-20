import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
import string
from tokenik import token
from logs import logs
from admin import admins
import time
from credentials import back
import users
import sqlite3

if os.path.isdir('databases') is False:
        os.mkdir('databases')

class menu(tk.Tk):
    
    if os.path.isdir('logs') is False:
        os.mkdir('logs')
    else:
        pass

    def __init__(self):
        tk.Tk.__init__(self)
        self.logi = logs()
        self.path_logs = "logs\\"
        tk.Tk.configure(self, bg="red")
        tk.Tk.geometry(self, "300x250")
        tk.Tk.title(self, "Smiglo Bank")
        tk.Label(self, text = "Welcome to Smiglo Bank", bg="pink", font = ("Algerian", 13)).pack()
        tk.Label(self, text = "").pack()
        self.but = tk.Button(self, text="Login", width=20, command=self.login)
        self.but.pack()
        tk.Label(self, text = "").pack()
        self.but2 = tk.Button(self, text="Register", width=20, command=self.register)
        self.but2.pack()
        tk.Label(self, text = "").pack()
        self.but3 = tk.Button(self, text="Forgot your credentials?", width=20, command=lambda:back(self, self.but3))
        self.but3.pack()

    # register system

    def register_user(self):
        self.but2.configure(state=tk.ACTIVE)
        self.check = self.choice.get()
        self.answer_check = self.answer.get()
        self.us = self.username.get()
        self.pas = self.password.get() 
        
        
        if self.check == questions[0]:
            messagebox.showerror("error","You have not choosen your secret question!")
        elif not self.answer_check:
            messagebox.showerror("error","You have not provided your answer!")
        elif not self.us:
            messagebox.showerror("error","You have not provided your login!")
        elif not self.pas:
            messagebox.showerror("error","You have not provided your password!")
        else:
            c = str(random.randint(1000, 9000))
            self.cash = 0
            self.username_info = self.username.get() 
            self.password_info = self.password.get() 
            self.code_info = c #random number rolled
            self.currency = "Not opened"
            self.question = self.check
            self.answer = self.answer_check
            self.token = "No token"
            self.acc_type = 'CUSTOMER'
               
                
            users.Register_validation(self.username_info, self.password_info, c, self.cash, self.currency, self.question, self.answer, self.token, "OFFLINE", self.acc_type)
                
            

            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            tk.Label(self.screen1, text="Registration succes", fg="green", font=("calibri", 11)).pack()
            messagebox.showinfo("Success", "your security code is: "+self.code_info)
            self.screen1.destroy()

    # register window

    def register(self):
        self.but2.configure(state=tk.DISABLED)

        self.screen1 = tk.Frame(self.master)
        global questions
        global screen1
        global choice
        global answer

        questions = ["Choose your secret question", "Your mother name", "Your favourite food", "Your best friend name"]
        self.choice = tk.StringVar(self)
        self.answer = tk.StringVar(self)
        self.choice.set(questions[0])
        global screen1

        self.screen1 = tk.Toplevel(self)
        self.screen1.title("register")
        self.screen1.geometry("350x300")
        self.screen1.protocol('WM_DELETE_WINDOW', lambda:self.close(self.but2, self.screen1))

        global username
        global password
        global username_entry
        global password_entry

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.screen1, text ="Please enter details").pack()
        tk.Label(self.screen1, text ="").pack()

        tk.Label(self.screen1, text ="Username *").pack()
        self.username_entry = tk.Entry(self.screen1, textvariable=self.username)
        self.username_entry.pack()

        tk.Label(self.screen1, text ="Password *").pack()
        self.password_entry = tk.Entry(self.screen1, show='*', textvariable=self.password)
        self.password_entry.pack()
        

        self.option_menu = tk.OptionMenu(self.screen1, self.choice, *questions)
        self.option_menu.pack()

        self.question_entry = tk.Entry(self.screen1, textvariable=self.answer)
        self.question_entry.pack()

        tk.Label(self.screen1, text ="").pack()
        tk.Button(self.screen1, text="register", width=20, command=self.register_user).pack()

    

    #login system

    def login_verify(self):
        self.but.configure(state=tk.ACTIVE)

        self.login_details = self.username2.get()
        self.password_details = self.password2.get()
        self.security_code_details = self.security_code.get()
        self.username_entry2.delete(0, tk.END)
        self.password_entry2.delete(0, tk.END)
        self.security_code_entry.delete(0, tk.END)
    
        users.verification(self.login_details, self.password_details, self.security_code_details)
        
    #login window

    def login(self):
        self.but.configure(state=tk.DISABLED)

        global screen2
        self.screen2 = tk.Toplevel(self)
        self.screen2.title("login")
        self.screen2.geometry("300x250")
        self.screen2.protocol('WM_DELETE_WINDOW', lambda:self.close(self.but, self.screen2))

        global username2
        global password2
        global security_code
        global username_entry2
        global password_entry2
        global security_code_entry

        self.username2 = tk.StringVar()
        self.password2 = tk.StringVar()
        self.security_code = tk.StringVar()

        tk.Label(self.screen2, text ="Username *").pack()
        self.username_entry2 = tk.Entry(self.screen2, textvariable=self.username2)
        self.username_entry2.pack()

        tk.Label(self.screen2, text ="Password *").pack()
        self.password_entry2 = tk.Entry(self.screen2, show='*', textvariable=self.password2)
        self.password_entry2.pack()

        tk.Label(self.screen2, text ="Security Code *").pack()
        self.security_code_entry = tk.Entry(self.screen2, textvariable=self.security_code)
        self.security_code_entry.pack()

        tk.Label(self.screen2, text ="").pack()
        self.login_but = tk.Button(self.screen2, text="login", width=20, command=self.token_check)
        self.login_but.pack()
    
    def close(self, buto, wind):
        self.buto = buto
        self.wind = wind
        self.buto.configure(state=tk.ACTIVE)
        self.wind.destroy()
    
        
    
    def token_check(self):
        global var
        global log 
        self.log = self.username2.get()
        self.var = tk.StringVar()
       
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE login=?",(self.log,))
        if cur.fetchone() is None:
            messagebox.showerror('error','User does not exsits')
        else:
            cur.execute("SELECT * FROM users WHERE login=?",(self.log,))
            rows = cur.fetchall()
            for row in rows:
                if row[9] == "ONLINE":
                    messagebox.showinfo("Online", "Account already online")
                else:
                    if row[8] == "No token":
                        self.login_verify()
                        self.screen2.destroy()
                    else:
                        self.t = token(self, self.log)
                        self.screen2.geometry("350x300")
                        tk.Label(self.screen2, text="").pack()
                        tk.Label(self.screen2, text='Provide your token').pack()
                        self.token_entry = tk.Entry(self.screen2, textvariable=self.var)
                        self.token_entry.pack()
                        self.login_but.configure(command=self.token_verify)       
    
    def token_verify(self):
        self.autho = self.var.get()
        if not self.token_entry:
            messagebox.showerror('error', 'empty gap')
        else:
            con = sqlite3.connect('databases\\main.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM users WHERE login=?',(self.log,))
            for row in cur.fetchall():
                if row[8] == self.autho:
                    self.t.destroy()
                    self.token_entry.destroy()
                    self.login_verify()
                    self.screen2.destroy()
                else:
                    messagebox.showerror('error','wrong token')

    