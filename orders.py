import sqlite3
import os
from datetime import datetime


def buy(login, product):
       
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        con = sqlite3.connect('databases\\users.db')
        cur = con.cursor()          
        cur.execute("INSERT INTO orders VALUES(NULL,(SELECT id FROM users WHERE login=?),(SELECT id FROM products WHERE name=?),?)",(login,product,date,))
        cur.execute("UPDATE users SET cash=cash-(SELECT price FROM products WHERE name=?) WHERE login=?",(product,login))
        con.commit()
        con.close()
