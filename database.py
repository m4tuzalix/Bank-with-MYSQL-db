import sqlite3
from tkinter import *


def AddProducts(Name, Owner, Price, Description):
    conn = sqlite3.connect('databases\\products.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO products VALUES (NULL,?,?,?,?)", (Name, Owner, Price, Description))
    conn.commit()
    conn.close

def ViewProducts():
    conn = sqlite3.connect('databases\\products.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    row = cur.fetchall()
    conn.commit()
    conn.close
    return row

def EditProducts(Name, Owner, Price, Description,id):
    conn = sqlite3.connect('databases\\products.db')
    cur = conn.cursor()
    cur.execute("UPDATE products SET name=?,owner=?,price=?,description=? WHERE id=?", (Name, Owner, Price, Description,id))
    conn.commit()
    conn.close

def DelProducts(id):
    conn = sqlite3.connect('databases\\products.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close

def SearchProducts(name,test):
    test=[]
    conn = sqlite3.connect('databases\\products.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE name LIKE ?", (name,))
    row = cur.fetchall()
    conn.commit()
    conn.close
    return row
    
