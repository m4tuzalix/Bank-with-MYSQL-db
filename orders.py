import sqlite3
import os
from datetime import datetime
from tkinter import messagebox


def buy(login, product):
       
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()          
        cur.execute("INSERT INTO orders VALUES(NULL,(SELECT id FROM users WHERE login=?),(SELECT id FROM products WHERE name=?),?)",(login,product,date,))
        cur.execute('SELECT * FROM users WHERE cash<(SELECT price FROM products WHERE name=?) and login=?',(product,login))
        if cur.fetchone():
                messagebox.showerror('error','Insufficient funds')
        else:
                cur.execute("UPDATE users SET cash=cash-(SELECT price FROM products WHERE name=?) WHERE login=?",(product,login))
                messagebox.showinfo('info','You have bought: '+str(product))
        con.commit()
        con.close()
