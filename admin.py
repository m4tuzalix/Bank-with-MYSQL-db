import tkinter as tk 
import os
from tkinter import messagebox
from logs import logs



class admins(tk.Tk):
    def __init__(self, login, password, code):
        self.login = login
        self.logs = logs()
        self.password = password
        self.code = code
        self.path_logs = "logs\\"
        tk.Tk.__init__(self)
        with open(self.path_admin+self.login, "r") as file:
            lines = file.readlines()
        with open(self.path_admin+self.login, "w") as file2:
            lines[3] = 'ONLINE'
            for x in lines:
                file2.write(x)
        tk.Tk.protocol(self,'WM_DELETE_WINDOW', self.offline_switch)
        tk.Tk.geometry(self,"400x400")
        tk.Tk.title(self, "Admin menu")
        tk.Label(self, text='Open user details').pack()
        self.info = tk.Entry(self, bg="yellow")
        self.info.pack()
        tk.Button(self, text='proceed', command=self.get_user).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Delete user account").pack()
        self.info2 = tk.Entry(self, bg="yellow")
        self.info2.pack()
        tk.Button(self, text='proceed', command=self.delete).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Suspend user account").pack()
        self.info3 = tk.Entry(self, bg="yellow")
        self.info3.pack()
        tk.Button(self, text='proceed', command=self.ban).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Unsuspend user account").pack()
        self.info4 = tk.Entry(self, bg="yellow")
        self.info4.pack()
        tk.Button(self, text='proceed', command=self.unban).pack()
    
    def offline_switch(self):
        with open(self.path_admin+self.login, "r") as file:
            lines = file.readlines()
        with open(self.path_admin+self.login, "w") as file2:
            lines[3] = 'OFFLINE'
            for x in lines:
                file2.write(x)
            self.destroy()
    
    def get_user(self):
        self.check = self.info.get()
        list_of_users = os.listdir(self.path_customers)

        if self.check in list_of_users:
            self.screen = tk.Toplevel(self)
            self.screen.geometry('450x400')
            self.text = tk.Text(self.screen)
            with open(self.path_customers+self.check, 'r') as file:
                lines = file.readlines()
                tk.Label(self.screen, text="login:      "+lines[0]).pack()
                tk.Label(self.screen, text="password:       "+lines[1]).pack()
                tk.Label(self.screen, text="security code:      "+lines[2]).pack()
                tk.Label(self.screen, text="Account balance:        "+lines[3]).pack()
                tk.Label(self.screen, text="Currency account:       "+lines[4]).pack()
                tk.Label(self.screen, text="Secret question:        "+lines[5]).pack()
                tk.Label(self.screen, text="Secret answer:      "+lines[6]).pack()
                tk.Label(self.screen, text="Token status:       "+lines[7]).pack()
                tk.Label(self.screen, text="online status:      "+lines[8]).pack()
                if "\n" in lines[8]:
                  tk.Label(self.screen, text="ACCOUNT SUSPENDED", fg="red").pack()  
        else:
            messagebox.showerror('error', 'No user found in database')

    def delete(self):
        self.check = self.info2.get()
        list_of_users = os.listdir(self.path_customers)
        if self.check in list_of_users:
            self.choice = messagebox.askquestion('delete', 'Do you want to delete '+self.check+" ?")
            if self.choice == 'yes':
                os.remove(self.path_customers+self.check)
            else:
                pass
        else:
            messagebox.showerror('error', 'No user in database')

    def ban(self):
        self.check = self.info3.get()
        list_of_users = os.listdir(self.path_customers)
        if self.check in list_of_users:
            self.choice2 = messagebox.askquestion('ban',"Do you want to suspend "+self.check)
            if self.choice2 == 'yes':
                with open(self.path_customers +self.check, 'r') as file:
                    lines = file.readlines()
                    if '\n' in lines[8]:
                        messagebox.showerror('error', 'Account has already been suspended')
                    else:
                        with open(self.path_customers +self.check, 'a') as file2:
                            file2.write('\n'+'BAN')
                            self.logs.suspend(self.check)
        else:
            messagebox.showerror('error', 'No user in database')

    def unban(self):
        self.check2 = self.info4.get()
        list_of_users = os.listdir(self.path_customers)
        if self.check2 in list_of_users:
            self.choice3 = messagebox.askquestion('ban',"Do you want to suspend "+self.check2)
            if self.choice3 == 'yes':
                with open(self.path_customers +self.check2, 'r') as file:
                    lines = file.readlines()
                with open(self.path_customers +self.check2, 'w') as file2:
                    if not '\n' in lines[8]:
                        messagebox.showerror('error', 'Account is not suspended')
                    else:
                        if 'OFFLINE' in lines[8]:
                            lines[8] = 'OFFLINE'
                            file2.write(lines[0])
                            file2.write(lines[1])
                            file2.write(lines[2])
                            file2.write(lines[3])
                            file2.write(lines[4])
                            file2.write(lines[5])
                            file2.write(lines[6])
                            file2.write(lines[7])
                            file2.write(lines[8])
                            self.logs.unsuspend(self.check)
                        else:
                            lines[8] = 'ONLINE'
                            file2.write(lines[0])
                            file2.write(lines[1])
                            file2.write(lines[2])
                            file2.write(lines[3])
                            file2.write(lines[4])
                            file2.write(lines[5])
                            file2.write(lines[6])
                            file2.write(lines[7])
                            file2.write(lines[8])
                            self.logs.unsuspend(self.check2)
        else:
            messagebox.showerror('error', 'No user in database') 

                    
                        
                   

               


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
        
        

    

    




  

            
            
            
                