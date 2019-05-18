import tkinter as tk 
import random
from tkinter import messagebox
from random import shuffle
import math
import time
from admin import bank_acc
from money import fiftyy,thirtyy,tenn
import sqlite3

class roulete(tk.Toplevel):
    def __init__(self, master, login):
        self.login = login
        tk.Toplevel.__init__(self, master)
        self.geometry('300x200')
        self.title('roulete')
        tk.Label(self, text="Choose game mode", font=('Arial', 12, 'bold')).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="50 percent chance", command=lambda: fifty(self, self.login)).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="30 percent chance", command=lambda: thirty(self, self.login)).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="10 percent chance", command=lambda: ten(self, self.login)).pack()

class change():
    def __init__(self):
        pass
    def change_window(self, option, option2):
        self.option = option
        self.option2 = option2
        self.option.deiconify()
        self.option2.destroy()
    def change_window_los(self, hide, unhide):
        self.hide = hide
        self.unhide = unhide

        self.hide.withdraw()
        self.unhide.deiconify()
        


class fifty(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.t = change()
        self.parent = parent
        self.bet = tk.StringVar()
        tk.Tk.__init__(self)
        self.parent.withdraw()
        self.geometry("200x200")
        self.entry = tk.Entry(self)
        self.entry.pack()
        tk.Button(self, text="Spin", command=self.check).pack()
        tk.Button(self, text="change mode", command=lambda: self.t.change_window(self.parent, self)).pack(side=tk.BOTTOM)

    def check(self):
        self.bet_score = float(self.entry.get())
        fiftyy(self.login,self.bet_score)


class thirty(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.t = change()
        self.parent = parent
        self.bet = tk.StringVar()
        tk.Tk.__init__(self)
        self.parent.withdraw()
        self.geometry("200x200")
        self.entry = tk.Entry(self)
        self.entry.pack()
        tk.Button(self, text="Spin", command=self.check).pack()
        tk.Button(self, text="change mode", command=lambda: self.t.change_window(self.parent, self)).pack(side=tk.BOTTOM)

    def check(self):
        self.bet_score = float(self.entry.get())
        thirtyy(self.login,self.bet_score)
                



class ten(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.t = change()
        self.parent = parent
        self.bet = tk.StringVar()
        tk.Tk.__init__(self)
        self.parent.withdraw()
        self.geometry("200x200")
        self.entry = tk.Entry(self)
        self.entry.pack()
        tk.Button(self, text="Spin", command=self.check).pack()
        tk.Button(self, text="change mode", command=lambda: self.t.change_window(self.parent, self)).pack(side=tk.BOTTOM)

    def check(self):
        self.bet_score = float(self.entry.get())
        tenn(self.login,self.bet_score)
                


class lotto(tk.Toplevel):
    def __init__(self, master, login, counter=0):
        self.login = login
        self.change = change()
        self.counter = counter
        self.path_customers = "customers\\"
        tk.Toplevel.__init__(self, master)
        self.geometry('350x300')
        tk.Label(self, text="Put 6 numbers").pack()
        self.entry = list(range(6))

        self.frame = tk.Frame(self, bg='green', bd=2, width=300, height=40, relief=tk.RIDGE)
        self.frame.pack(side=tk.TOP)
        a = -1
        b = 0 
        for y in range(6):   #///// loop for entries to provide the numbers to roll
            a = a+1
            b = b+1
            self.entry[a] = tk.Entry(self.frame, width=5,bg='yellow')
            self.entry[a].grid(row=0, column=b)
        
        for x in range(4):
            tk.Label(self, text="").pack()
        
        self.info = tk.Label(self, text="Numbers")
        self.info.pack()
        tk.Label(self, text="").pack()
        self.but = tk.Button(self, text="check", command=self.three_try)
        self.but.pack()
        self.info2 = tk.Label(self, text="You guess")
        self.info2.pack()

    def one_try(self):
        self.roll_numbers()
        if self.counter == 1:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.change.change_window_los(self, lotto_los(self, self.login))
            
    def three_try(self):
        self.roll_numbers()
        if self.counter == 3:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.change.change_window_los(self, lotto_los(self, self.login))

    def five_try(self):
        self.roll_numbers()
        if self.counter == 5:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.change.change_window_los(self, lotto_los(self, self.login))

    def ten_try(self):
        self.roll_numbers()
        if self.counter == 10:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.change.change_window_los(self, lotto_los(self, self.login))

        

    def roll_numbers(self):
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        self.info2.config(text="No score")
        lottery = list(range(1,49))
        numbers = []
        hit = []
        entries = [(self.entry[0].get()), (self.entry[1].get()), (self.entry[2].get()), (self.entry[3].get()), (self.entry[4].get()), (self.entry[5].get())]
        double_check = set(entries)  #### set returns value without duplicates


        if len(double_check) != len(entries): ### if duplicates exist, double_check length is lower then the original length of the list
            messagebox.showerror('error', 'Value cannot be doubled!')
        elif any(int(e)<0 for e in entries):
            messagebox.showerror('error', 'Value cannot be negative')
        elif any(int(e)==0 for e in entries):
            messagebox.showerror('error', 'Value cannot be zero')
        
    
        else:
            for i in range(6):
                shuffle(lottery) ## each time changes the list order
                x = lottery.pop() ## takes one random number         ### REPEATS 6 TIMES
                numbers.append(x) ## adds it to 'numbers' 
                for entry in entries:
                    if int(entry) == numbers[i]:
                        hit.append(int(entry))
                        self.info2.config(text='You have guessed: '+str(hit))
        self.info.config(text=str(numbers))
        if len(hit) == 3:
            win = random.randint(1000,2000)
            messagebox.showinfo('win', 'You have guess 3 numbers, won: '+str(win))
            cur.execute('UPDATE users SET cash=cash+? WHERE login=?',(win,self.login))
        elif len(hit) == 4:
            win = random.randint(10000,20000)
            messagebox.showinfo('win', 'You have guess 4 numbers, won: '+str(win))
            cur.execute('UPDATE users SET cash=cash+? WHERE login=?',(win,self.login))
        
        elif len(hit) == 5:
            win = random.randint(100000,200000)
            messagebox.showinfo('win', 'You have guess 5 numbers, won: '+str(win))
            cur.execute('UPDATE users SET cash=cash+? WHERE login=?',(win,self.login))

        elif len(hit) == 6:
            win = random.randint(1000000,10000000)
            messagebox.showinfo('win', 'You have guess all numbers!!!!!, won: '+str(win))
            cur.execute('UPDATE users SET cash=cash+? WHERE login=?',(win,self.login))
        con.commit()
        con.close()    
        self.counter = self.counter + 1
        
    
class lotto_los(tk.Toplevel):
    def __init__(self, master, login):
        self.login = login
        tk.Toplevel.__init__(self, master)
        self.geometry('350x300')
        tk.Label(self, text="Pick how many tries you want").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="1 try", command=self.one).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="3 tries", command=self.three).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="5 tries", command=self.five).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="10 tries", command=self.ten).pack()
        
        
    def one(self):
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.login,))
        for row in cur.fetchall():
            if row[4] < 100:
                messagebox.showerror('error', 'No funds')
            elif row[4] > 100:
                cur.execute('UPDATE users SET cash=cash-? WHERE login=?',(100,self.login))
                con.commit()
                con.close()
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.ten_try)
                self.t
                self.withdraw()
                    
        

    def three(self):
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.login,))
        for row in cur.fetchall():
            if row[4] < 300:
                messagebox.showerror('error', 'No funds')
            elif row[4] > 300:
                cur.execute('UPDATE users SET cash=cash-? WHERE login=?',(300,self.login))
                con.commit()
                con.close()
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.ten_try)
                self.t
                self.withdraw()
                    

    def five(self):
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.login,))
        for row in cur.fetchall():
            if row[4] < 500:
                messagebox.showerror('error', 'No funds')
            elif row[4] > 500:
                cur.execute('UPDATE users SET cash=cash-? WHERE login=?',(500,self.login))
                con.commit()
                con.close()
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.ten_try)
                self.t
                self.withdraw()
                    

    def ten(self):
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.login,))
        for row in cur.fetchall():
            if row[4] < 1000:
                messagebox.showerror('error', 'No funds')
            elif row[4] > 1000:
                cur.execute('UPDATE users SET cash=cash-? WHERE login=?',(1000,self.login))
                con.commit()
                con.close()
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.ten_try)
                self.t
                self.withdraw()
                
                    
        
    
    
    
    

            
        
        
                

        
            
        
            




        
    