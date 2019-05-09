import sqlite3
from tkinter import messagebox
from banking import bank

check = []

def users():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, login TEXT(15), password TEXT(15), sec_code TEXT(4), cash FLOAT, currency TEXT, question TEXT, answer TEXT, token TEXT, status TEXT, acc_type TEXT(8))')
    con.commit()
    con.close()

## REGISTRY PART

def CreateUser(login, password, sec_code, cash, currency, question, answer, token, status, acc_type):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users VALUES (NULL,?,?,?,?,?,?,?,?,?,?)', (login, password, sec_code, cash, currency, question, answer, token, status, acc_type))
    con.commit()
    con.close()

def Register_validation(login, password, sec_code, cash, currency, question, answer, token, status, acc_type):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE login=?",(login,))
    if cur.fetchone():
        messagebox.showerror('error', 'Login already exists, choose another')
    else:
        CreateUser(login, password, sec_code, cash, currency, question, answer, token, status, acc_type)
        con.commit()
        con.close()

#### Validation part

def OpenToken(nick, number):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET token=? WHERE login=?", (number,nick))
    con.commit()
    con.close()
    


def verification(nick, pas, code):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE login=? AND password=? AND sec_code=?", (nick,pas,code))
    if cur.fetchone():
        bank(nick,pas,code)
    else:
        messagebox.showerror('error', 'Wrong credentials')
        con.commit()
        con.close()

###### ONLINE and OFFLINE part

def online(login):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('UPDATE user SET status=? WHERE login=?',('ONLINE',login))
    con.commit()
    con.close()

def offline(login):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('UPDATE user SET status=? WHERE login=?',('OFFLINE',login))
    con.commit()
    con.close()







users()

