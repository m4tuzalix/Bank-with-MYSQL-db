import sqlite3
from tkinter import messagebox

#/// Custom currency


def deposit_cash(amount,login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET cash=cash+? WHERE login=?", (amount,login,))
    con.commit()
    con.close()

def withdraw_cash(amount,login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE cash<? AND login=?",(amount,login))
    con.commit()
    if cur.fetchone():
        messagebox.showerror('error','Insufficient funds')
    else:
        cur.execute("UPDATE users SET cash=cash-? WHERE login=?", (amount,login,))
        con.commit()
        con.close()

def cash_check(login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE login=?", (login,))
    rows = cur.fetchall()  # ///////// fetchal returns all rows from provided login
    for row in rows: #//// checking all rows in login provided
        messagebox.showinfo('info','Your balance: '+str(row[4]))  #/// printing row[4] which is cash 
    con.commit()
    con.close()

#//// Transfers

def send_cash(amount,login, customer):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    funds_check = cur.execute("SELECT * FROM users WHERE cash<? AND login=?",(amount,login,)) #//// checks if user has enough money. If returns True then he doesn't have
    if funds_check.fetchone():
        messagebox.showerror('error', 'No funds to make transfer')
    else:
        cur.execute("UPDATE users SET cash=cash-? WHERE login=?", (amount,login,)) #/// Takes money from sender
        cur.execute("UPDATE users SET cash=cash+? WHERE login=?", (amount,customer,)) #//// Transfers the money taken from sender to the customer
        con.commit()
        con.close()

#///// currency

def open_account(login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("ALTER TABLE users RENAME TO tmp")
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, login TEXT(15), password TEXT(15), sec_code TEXT(4), cash FLOAT, currency FLOAT, question TEXT, answer TEXT, token TEXT, status TEXT, acc_type TEXT(8))")
    cur.execute('INSERT INTO users SELECT * FROM tmp')
    cur.execute('UPDATE users SET currency=? WHERE login=?',(0, login))
    cur.execute('DROP TABLE tmp')
    con.commit()
    con.close()

    

def usd_deposit(amount,login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET currency=currency+? WHERE login=?", (amount,login,))
    con.commit()
    con.close()

def withdraw_usd(amount,login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE currency<? AND login=?",(amount,login))
    con.commit()
    if cur.fetchone():
        messagebox.showerror('error','Insufficient funds')
    else:
        cur.execute("UPDATE users SET currency=currency-? WHERE login=?", (amount,login,))
        con.commit()
        con.close()

def pln_to_currency(amount, login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE cash<? AND login=?",(amount,login))
    con.commit()
    if cur.fetchone():
        messagebox.showerror('error','Insufficient funds')
    else:
        cur.execute("UPDATE users SET cash=cash-? WHERE login=?", (amount,login,))
        cur.execute("UPDATE users SET currency=round(currency+?/?,?) WHERE login=?", (amount, 3.70,2,login,))
        con.commit()
        con.close()

def currency_transfer(customer,login,amount):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE login=?",(customer,))
    if cur.fetchone():
        cur.execute("SELECT * FROM users WHERE login=?",(customer,))
        for row in cur.fetchall():
            if row[5] == 'Not opened': #////// checks customer row if currency has been opened
                messagebox.showerror('error','User has not opened currency account yet')
            else:
                cur.execute("SELECT * FROM users WHERE currency<? AND login=?", (amount,login))
                if cur.fetchone(): #///// checks user currency amount if sufficient to make payement
                    messagebox.showerror('error','Insufficient funds')
                else:
                    cur.execute("UPDATE users SET currency=currency-? WHERE login=?", (amount,login,))          #//////// Takes amount from user and transfers to customer
                    cur.execute("UPDATE users SET currency=currency+? WHERE login=?", (amount, customer))
    else:
        messagebox.showerror('error','user does not exist')
    con.commit()
    con.close()

#////// online and offline status

def status(login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE login=?',(login,))
    for row in cur.fetchall():
        if row[9] == 'OFFLINE':
            cur.execute('UPDATE users SET status=? WHERE login=?',('ONLINE', login))
        else:
            cur.execute('UPDATE users SET status=? WHERE login=?',('OFFLINE', login))
    con.commit()
    con.close()

#/// TOKEN OPEN

def Token_open(login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute('UPDATE users SET token=? WHERE login=?',('Activated',login,))
    con.commit()
    con.close()

def Token_close(login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute('UPDATE users SET token=? WHERE login=?',('No token',login,))
    con.commit()
    con.close()

#///// Admin or customer check

def Account_type(login):
    con = sqlite3.connect('databases\\users.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE login=?',(login,))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows