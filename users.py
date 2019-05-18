import sqlite3
from tkinter import messagebox
from banking import bank
from admin import admins
check = []

def users():
    con = sqlite3.connect('databases\\main.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, login TEXT(15), password TEXT(15), sec_code TEXT(4), cash FLOAT, currency TEXT, question TEXT, answer TEXT, token TEXT, status TEXT, acc_type TEXT(8))')
    cur.execute("CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT, owner TEXT,  price INTEGER, description TEXT)")
    cur.execute('CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, UserId INTEGER, ProductId INTEGER, Date TEXT, FOREIGN KEY (UserId) REFERENCES users(id), FOREIGN KEY (ProductId) REFERENCES products(id))')
    con.commit()
    con.close()

def ShowUser():
    con = sqlite3.connect('databases\\main.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    ret = cur.fetchall()
    return ret



## REGISTRY PART

def CreateUser(login, password, sec_code, cash, currency, question, answer, token, status, acc_type):
    con = sqlite3.connect('databases\\main.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users VALUES (NULL,?,?,?,?,?,?,?,?,?,?)', (login, password, sec_code, cash, currency, question, answer, token, status, acc_type))
    con.commit()
    con.close()

def Register_validation(login, password, sec_code, cash, currency, question, answer, token, status, acc_type):
    con = sqlite3.connect('databases\\main.db')
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
    con = sqlite3.connect('databases\\main.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET token=? WHERE login=?", (number,nick))
    con.commit()
    con.close()
    


def verification(nick, pas, code):
    con = sqlite3.connect('databases\\main.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE login=? AND password=? AND sec_code=?", (nick,pas,code))
    if cur.fetchone():
        cur.execute("SELECT * FROM users WHERE login=? AND password=? AND sec_code=?",(nick,pas,code))
        for row in cur.fetchall():
            if row[10] == 'CUSTOMER':
                bank(nick,pas,code)
            elif row[10] == 'ADMIN':
                admins(nick,pas,code)
            else:
                messagebox.showerror('error','You have been banned')
    else:
        messagebox.showerror('error', 'Wrong credentials')
        con.commit()
        con.close()

###### ONLINE and OFFLINE part

def online(login):
    con = sqlite3.connect('databases\\main.db')
    cur = con.cursor()
    cur.execute('UPDATE user SET status=? WHERE login=?',('ONLINE',login))
    con.commit()
    con.close()

def offline(login):
    con = sqlite3.connect('databases\\main.db')
    cur = con.cursor()
    cur.execute('UPDATE user SET status=? WHERE login=?',('OFFLINE',login))
    con.commit()
    con.close()







users()

