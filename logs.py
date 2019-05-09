from datetime import datetime
import sqlite3
class logs():
    def __init__(self):
        self.t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.path_logs = "logs\\"
        pass
    
    def depo_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Deposit: "+str(self.value)+" pln"+"\n")
        file.close

    def depo_usd_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Deposit: "+str(self.value)+" usd"+"\n")
        file.close

    def with_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Withdraw: "+str(self.value)+" pln"+"\n") 
        file.close

    def with_usd_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Withdraw: "+str(self.value)+" usd"+"\n") 
        file.close

    def transfer_logs(self, name, customer, value):
        self.name = name
        self.customer = customer
        self.value = value
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Transfered "+str(self.value)+".pln to"+" "+str(self.customer)+"\n")
        file.close
        file = open(self.path_logs+self.customer+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Received transfer from "+str(self.name)+" "+str(self.value)+".pln"+"\n")
        file.close

    def transfer_usd_logs(self, name, customer, value):
        self.name = name
        self.customer = customer
        self.value = value
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Currency transfer for "+str(self.value)+" usd to"+" "+str(self.customer)+"\n")
        file.close
        file = open(self.path_logs+self.customer+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Received currency transfer from "+str(self.name)+" "+str(self.value)+" usd"+"\n")
        file.close

    def token_logs_on(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Token activated"+"\n")

    def token_logs_off(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Token deactivated"+"\n")

    def currency_logs_on(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Currency account activated"+"\n")

    def log_on(self, name):
        self.name = name
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE login=?',(self.name,))
        for row in cur.fetchall():
            if row[9] == 'OFFLINE':
                cur.execute('UPDATE users SET status=? WHERE login=?',('ONLINE', self.name))
                file = open(self.path_logs+self.name+"_logs", "a")
                file.write("<"+self.t+">"+" "+"Logged in"+"\n")
            else:
                file = open(self.path_logs+self.name+"_logs", "a")
                file.write("<"+self.t+">"+" "+"Logged out"+"\n")

    def suspend(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Account suspended"+"\n")

    def unsuspend(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Account unsuspended"+"\n")

        


           
        