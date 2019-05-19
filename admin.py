import tkinter as tk 
import os
from tkinter import messagebox
from logs import logs
from gui import gui
from money import status
from collections import OrderedDict
import sqlite3
from money import admin_list, ban_unban


class admins(tk.Tk):
    def __init__(self,nick,password,code):
        self.nick = nick
        self.password = password
        self.code = code 
        self.path_logs = "logs\\"
        tk.Tk.__init__(self)
        tk.Tk.title(self,'managament app')
        tk.Tk.geometry(self,'760x575+0+0')
        tk.Tk.configure(self,bg='blue')


    #frames
        Main = tk.Frame(self, bg='green')
        Main.grid()

        Header = tk.Frame(Main, bg='green', bd=2, padx=54, pady=8, relief=tk.RIDGE) #////// title space
        Header.pack(side=tk.TOP)

        self.Header_text = tk.Label(Header, font=('times new roman', 40, 'bold'), text="ADMIN MENU", bg='green')
        self.Header_text.grid()

        ClickFrame = tk.Frame(Main, bd=2, width=970, height=70, padx=18, pady=10, bg='blue', relief=tk.RIDGE) #//// buttons space
        ClickFrame.pack(side=tk.BOTTOM)

        Data = tk.Frame(Main, bd=1, width=1300, height=400, padx=20, pady=20, relief=tk.RIDGE, bg='white') #////// content space
        Data.pack(side=tk.BOTTOM)

        DataLeft = tk.LabelFrame(Data, bd=1, width=600, height=200, padx=20, relief=tk.RIDGE, bg='yellow', text='User information\n', font=('arial', 20, 'bold'))
        DataLeft.pack(side=tk.LEFT)

        DataRight = tk.LabelFrame(Data, bd=1, width=450, height=300, padx=31, pady=3, relief=tk.RIDGE, bg='red',  text='User details\n', font=('arial', 20, 'bold'))
        DataRight.pack(side=tk.RIGHT)
    
    #///// loop to display 10 entries and sign them up   
        a = -1
        self.info = list(range(10))
        for x in range(10):
            a = a +1
            names =['login','password','code','cash','currency','question','answer','token','status','acc_type']  
            tk.Label(DataLeft, text=names[a], bg='yellow', bd=1).grid(row=a, column=0)
            self.info[a] = tk.Entry(DataLeft, bg="yellow")
            self.info[a].grid(row=a, column=1)
            
    #///// scrollbar where data from database is displayed

        Details = tk.Scrollbar(DataRight)
        Details.grid(row=0, column=1, padx=8)
        global ProductList
        ProductList = tk.Listbox(DataRight, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=Details.set)
        ProductList.bind('<<ListboxSelect>>', self.ChooseUser)
        ProductList.grid(row=0, column=0, padx=8)
        Details.configure(command=ProductList.yview)

        tk.Button(ClickFrame, text='refresh', command=self.get_user).grid(row=0, column=1)
        tk.Button(ClickFrame, text='ban', command=self.ban_unban).grid(row=0, column=2)
        tk.Button(ClickFrame, text='clear', command=self.list_clear).grid(row=0, column=3)
        tk.Button(ClickFrame, text='delete', command=self.delete).grid(row=0, column=4)
        tk.Button(ClickFrame, text='shop', command=lambda:gui(self,self.nick)).grid(row=0, column=5)
    
    
#////// functions

    def offline_switch(self):
        status(self.login)
        self.destroy()

    def list_clear(self):
        a = -1
        for x in range(10):
            a = a+1
            self.info[a].delete(0,tk.END)

    
    def get_user(self):
        ProductList.delete(0,tk.END)
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT login FROM users')
        rows = cur.fetchall()
        for row in rows:
            ProductList.insert(tk.END,row,str(''))
        con.commit()
        con.close()
            

    def delete(self):
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        messagebox.askyesno('info','Do you want to delete: '+str(particular_id[0]+'?'))
        if 'yes':
            cur.execute('DELETE FROM users WHERE login=?',(particular_id[0],))
            self.get_user()
        else: 
            pass
        con.commit()
        con.close()

    def ban_unban(self):
        ban_unban(self.info[0].get())
                    
    def ChooseUser(self,Event=None):
        b = -1
        selection = ProductList.curselection()[0]
        global particular_id
        particular_id = ProductList.get(selection)
        for row in admin_list(particular_id[0]): #///// all rows from given login are returned and loop executes each one separately
            if len(particular_id)==0:
                self.info[b].delete(0,tk.END)
            else:
                for p in range(10): #//// second loop checking the number of row and then assigning it to the specific field
                    b = b+1
                    self.info[b].delete(0,tk.END)
                    self.info[b].insert(tk.END,row[b+1]) #//// +1 because we want to avoid displaying id
        self.get_user()
                    
                                 
                   

               


class admin_chat(tk.Toplevel):
    def __init__(self, master, login, haslo, kod):
        self.path_customers = 'customers\\'
        self.path_logs = "logs\\"
        self.path_admin = "admin\\"
        self.login = login
        self.haslo = haslo
        self.kod = kod
        tk.Toplevel.__init__(self, master)
        self.geometry("300x200")
        self.title("Admin chat")
        tk.Label(self, text="Check on-line Admins").pack()
        self.action = tk.Button(self, text="Go", command=self.who_is_online)
        self.action.pack()
        self.info = tk.Label(self, text='')
        self.info.pack()
        


    def who_is_online(self):
        online = []
        for files in os.listdir(self.path_admin):
            with open(self.path_admin+files, "r") as file:
                lines = file.readlines()
            if lines[3] == "ONLINE":
                online.append(files)
                self.info.config(text='Admin is online: '+str(online), fg="green")
                file.close
            else:
                self.info.config(text="admin is offline", fg="red")

class bank_acc():
    def __init__(self, path, amount):
        self.path = path
        self.amount = amount
        with open(self.path, 'r') as file:
            lines=file.readlines()
        with open(self.path, 'w') as file:
            lines[0]=str(float(lines[0])+float(self.amount))
            file.write(lines[0])
            file.close
        
        

    

    




  

            
            
            
                