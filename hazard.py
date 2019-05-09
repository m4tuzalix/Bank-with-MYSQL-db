import tkinter as tk 
import random
from tkinter import messagebox
from random import shuffle
import math
import time
from admin import bank_acc


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
        self.path_customers = "customers\\"
        self.path_bank = 'bank_account\\bank'
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
        self.number = random.randint(1,2)
        self.bet_score = float(self.entry.get())
        with open(self.path_customers+self.login, "r") as file:
            lines = file.readlines()
            if float(lines[3]) < self.bet_score:
                messagebox.showerror('error', 'no funds')
            else:
                if self.number == 1:
                    with open(self.path_customers+self.login, "w") as file2:
                        for x in lines:
                            file2.write(x)
                        messagebox.showinfo('great','You won: '+str(round(self.bet_score/5)))
                else:
                    with open(self.path_customers+self.login, "w") as file2:
                        lines[3]=str(float(lines[3])-self.bet_score)+'\n'
                        for x in lines:
                            file2.write(x)
                        messagebox.showinfo('loose', "you lost")
                bank_acc(self.path_bank,self.bet_score)


class thirty(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.path_customers = "customers\\"
        self.path_bank = 'bank_account\\bank'
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
        self.number = random.randint(1,5)
        self.bet_score = float(self.entry.get())
        with open(self.path_customers+self.login, "r") as file:
            lines = file.readlines()
            if float(lines[3]) < self.bet_score:
                messagebox.showerror('error', 'no funds')
            else:
                if self.number == 1:
                    with open(self.path_customers+self.login, "w") as file2:
                        lines[3]=str(float(lines[3])+round(self.bet_score/2))+'\n'
                        for x in lines:
                            file2.write(x)
                        messagebox.showinfo('great','You won: '+str(round(self.bet_score/2)))
                else:
                    with open(self.path_customers+self.login, "w") as file2:
                        lines[3]=str(float(lines[3])-self.bet_score)+'\n'
                        for x in lines:
                            file2.write(x)
                        messagebox.showinfo('loose', "you lost")
                bank_acc(self.path_bank,self.bet_score)



class ten(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.path_customers = "customers\\"
        self.path_bank = 'bank_account\\bank'
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
        self.number = random.randint(1,10)
        self.bet_score = float(self.entry.get())
        with open(self.path_customers+self.login, "r") as file:
            lines = file.readlines()
            if float(lines[3]) < self.bet_score:
                messagebox.showerror('error', 'no funds')
            else:
                if self.number == 1:
                    with open(self.path_customers+self.login, "w") as file2:
                        lines[3]=str(float(lines[3])+round(self.bet_score))+'\n'
                        for x in lines:
                            file2.write(x)
                        messagebox.showinfo('great','You won: '+str(round(self.bet_score)))
                else:
                    with open(self.path_customers+self.login, "w") as file2:
                        lines[3]=str(float(lines[3])-self.bet_score)+'\n'
                        for x in lines:
                            file2.write(x)
                        messagebox.showinfo('loose', "you lost")
                bank_acc(self.path_bank,self.bet_score)


class lotto(tk.Toplevel):
    def __init__(self, master, login, counter=0):
        self.login = login
        self.change = change()
        self.counter = counter
        self.path_customers = "customers\\"
        tk.Toplevel.__init__(self, master)
        self.geometry('350x300')
        tk.Label(self, text="Put 6 numbers").pack()
        self.entry1 = tk.Entry(self, bg='yellow')
        self.entry2 = tk.Entry(self, bg='yellow')
        self.entry3 = tk.Entry(self, bg='yellow')
        self.entry4 = tk.Entry(self, bg='yellow')
        self.entry5 = tk.Entry(self, bg='yellow')
        self.entry6 = tk.Entry(self, bg='yellow')
        self.entry1.place(x=60, y=50, width=30)
        self.entry2.place(x=100, y=50, width=30)
        self.entry3.place(x=140, y=50, width=30)
        self.entry4.place(x=180, y=50, width=30)
        self.entry5.place(x=220, y=50, width=30)
        self.entry6.place(x=260, y=50, width=30)
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
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
        self.info2.config(text="No score")
        lottery = list(range(1,49))
        numbers = []
        hit = []
        entries = [(self.entry1.get()), (self.entry2.get()), (self.entry3.get()), (self.entry4.get()), (self.entry5.get()), (self.entry6.get())]
        double_check = set(entries)  #### set returns value without duplicates
        file=open(self.path_customers+self.login, 'r')
        lines=file.readlines()

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
            with open(self.path_customers+self.login, 'w') as file:
                lines[3]=str(float(lines[3])+float(win))+'\n'
                for x in lines:
                    file.write(x)
        elif len(hit) == 4:
            win = random.randint(10000,20000)
            messagebox.showinfo('win', 'You have guess 4 numbers, won: '+str(win))
            with open(self.path_customers+self.login, 'w') as file:
                lines[3]=str(float(lines[3])+float(win))+'\n'
                for x in lines:
                    file.write(x)
        
        elif len(hit) == 5:
            win = random.randint(100000,200000)
            messagebox.showinfo('win', 'You have guess 5 numbers, won: '+str(win))
            with open(self.path_customers+self.login, 'w') as file:
                lines[3]=str(float(lines[3])+float(win))+'\n'
                for x in lines:
                    file.write(x)

        elif len(hit) == 6:
            win = random.randint(1000000,10000000)
            messagebox.showinfo('win', 'You have guess all numbers!!!!!, won: '+str(win))
            with open(self.path_customers+self.login, 'w') as file:
                lines[3]=str(float(lines[3])+float(win))+'\n'
                for x in lines:
                    file.write(x)
        self.counter = self.counter + 1
        
    
class lotto_los(tk.Toplevel):
    def __init__(self, master, login):
        self.login = login
        self.path_customers = "customers\\"
        self.path_bank = 'bank_account\\bank'
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
        with open(self.path_customers+self.login, 'r') as file:
            lines = file.readlines()
        if float(lines[3]) < 100:
            messagebox.showerror('error', 'No funds')
        elif float(lines[3]) > 100:
            with open(self.path_customers+self.login, 'w') as file2:
                lines[3]=str(float(lines[3])-100.0)+'\n'
                for x in lines:
                    file2.write(x)
            
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.one_try)
                self.t
                self.withdraw()
                bank_acc(self.path_bank, 100)
        

    def three(self):
        with open(self.path_customers+self.login, 'r') as file:
            lines = file.readlines()
        if float(lines[3]) < 300:
            messagebox.showerror('error', 'No funds')
        elif float(lines[3]) > 300:
            with open(self.path_customers+self.login, 'w') as file2:
                lines[3]=str(float(lines[3])-300.0)+'\n'
                for x in lines:
                    file2.write(x)
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.three_try)
                self.t
                self.withdraw()
                bank_acc(self.path_bank, 300)

    def five(self):
        with open(self.path_customers+self.login, 'r') as file:
            lines = file.readlines()
        if float(lines[3]) < 500:
            messagebox.showerror('error', 'No funds')
        elif float(lines[3]) > 500:
            with open(self.path_customers+self.login, 'w') as file2:
                lines[3]=str(float(lines[3])-500.0)+'\n'
                for x in lines:
                    file2.write(x)
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.five_try)
                self.t
                self.withdraw()
                bank_acc(self.path_bank, 500)

    def ten(self):
        with open(self.path_customers+self.login, 'r') as file:
            lines = file.readlines()
        if float(lines[3]) < 1000:
            messagebox.showerror('error', 'No funds')
        elif float(lines[3]) > 1000:
            with open(self.path_customers+self.login, 'w') as file2:
                lines[3]=str(float(lines[3])-1000.0)+'\n'
                for x in lines:
                    file2.write(x)
                self.t = lotto(self, self.login)
                self.b = self.t.but
                self.b.configure(command=self.t.ten_try)
                self.t
                self.withdraw()
                bank_acc(self.path_bank, 1000)
        
    
    
    
    

            
        
        
                

        
            
        
            




        
    