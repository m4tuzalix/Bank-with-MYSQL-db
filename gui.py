from tkinter import *
from tkinter import messagebox
import database
import random
from collections import OrderedDict
import sqlite3
class gui(Toplevel):
    def __init__(self,master, nick):
        self.nick = nick
        Toplevel.__init__(self,master)
        Tk.title(self,'managament app')
        Tk.geometry(self,'970x600+0+0')
        Tk.configure(self,bg='blue')

        #containers for data
        self.prodName = StringVar()
        self.prodOwner = StringVar()
        self.prodPrice = StringVar()
        self.prodDescription = StringVar()

        

        #frames
        Main = Frame(self, bg='green')
        Main.grid()

        Header = Frame(Main, bg='green', bd=2, padx=54, pady=8, relief=RIDGE) #////// title space
        Header.pack(side=TOP)

        self.Header_text = Label(Header, font=('times new roman', 40, 'bold'), text="managament", bg='green')
        self.Header_text.grid()

        ClickFrame = Frame(Main, bd=2, width=1350, height=70, padx=18, pady=10, bg='green', relief=RIDGE) #//// buttons space
        ClickFrame.pack(side=BOTTOM)

        Data = Frame(Main, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg='white') #////// content space
        Data.pack(side=BOTTOM)

        DataLeft = LabelFrame(Data, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg='green', text='Product information\n', font=('arial', 20, 'bold'))
        DataLeft.pack(side=LEFT)

        DataRight = LabelFrame(Data, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg='green',  text='Product details\n', font=('arial', 20, 'bold'))
        DataRight.pack(side=RIGHT)
        ##entries and labels

        self.productName = Label(DataLeft, text='Product name')
        self.productName.grid(row=1, column=0, sticky=W)
        self.entry_name = Entry(DataLeft, textvariable=self.prodName, width=39)
        self.entry_name.grid(row=1, column=1)

        self.productOwner = Label(DataLeft, text='Product owner')
        self.productOwner.grid(row=2, column=0, sticky=W)
        self.entry_Owner = Entry(DataLeft, textvariable=self.prodOwner, width=39)
        self.entry_Owner.grid(row=2, column=1)
        
        self.productPrice = Label(DataLeft, text='Product price')
        self.productPrice.grid(row=3, column=0, sticky=W)
        self.entry_price = Entry(DataLeft, textvariable=self.prodPrice, width=39)
        self.entry_price.grid(row=3, column=1)

        self.productDescription = Label(DataLeft, text='Product description')
        self.productDescription.grid(row=4, column=0, sticky=W)
        self.entry_Description = Entry(DataLeft, textvariable=self.prodDescription, width=39)
        self.entry_Description.grid(row=4, column=1)
        
        ### labels editing loop
        global test
        test = {self.productDescription,
        self.productOwner, self.productPrice, self.productName}
        for x in test:
            x.configure(bg='green', padx=2, pady=2, font=('times new roman', 15, 'bold'))

        ## details window
        Details = Scrollbar(DataRight)
        Details.grid(row=0, column=1, padx=8)
        global ProductList
        ProductList = Listbox(DataRight, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=Details.set)
        ProductList.bind('<<ListboxSelect>>', self.ChooseProduct)
        ProductList.grid(row=0, column=0, padx=8)
        Details.configure(command=ProductList.yview)

        ##buttons

        self.buttonAdd = Button(ClickFrame, text='new', command=self.AddProducts)
        self.buttonAdd.grid(row=0, column=0)

        self.buttonDel = Button(ClickFrame, text='view', command=self.Show_product)
        self.buttonDel.grid(row=0, column=1)

        self.buttonEdit = Button(ClickFrame, text='delete', command=self.Del_product)
        self.buttonEdit.grid(row=0, column=2)

        self.buttonEdit = Button(ClickFrame, text='edit', command=self.Edit)
        self.buttonEdit.grid(row=0, column=3)

        self.buttonExit = Button(ClickFrame, text='exit', command=self.exit)
        self.buttonExit.grid(row=0, column=4)

        buttons = {self.buttonAdd, self.buttonDel, self.buttonEdit, self.buttonExit}
        for b in buttons:
            b.configure(width=5, height=1, bd=4, font=('times new roman', 20, 'bold'))

        ### functions

    def exit(self):
        prompt = messagebox.askyesno('info',"Are you sure to exit?")
        if prompt == YES:
            self.destroy()
            return
    
    def AddProducts(self):
    
        database.AddProducts(self.entry_name.get(), self.entry_Owner.get(),  self.entry_price.get(), self.entry_Description.get())
        ProductList.delete(0,END)
        ProductList.insert(END,(self.prodName.get(), self.prodOwner.get(),  self.prodPrice.get(), self.prodDescription.get()))
        self.Show_product()
        
    def Show_product(self):    
        ProductList.delete(0,END)
        con = sqlite3.connect('databases\\main.db')
        cur = con.cursor()
        cur.execute('SELECT id,name FROM products')
        rows = cur.fetchall()
        for row in rows:
            ProductList.insert(END,row,str(''))
        con.commit()
        con.close()
        

    def Del_product(self):
        global selection
        selection = ProductList.curselection()[0]
        particular_id = ProductList.get(selection)
        database.DelProducts(particular_id[0])
        self.Show_product()

    def ChooseProduct(self,Event=None):
        a = 0
        selection = ProductList.curselection()[0]
        particular_id = ProductList.get(selection)
        list_of_entries = {self.entry_Owner:2,self.entry_price:3,self.entry_name:1,self.entry_Description:4}
        for x in OrderedDict(sorted(list_of_entries.items(), key=lambda t:t[1])):
            for row in database.product_list(particular_id[0]):
                if len(particular_id)==0:
                    x.delete(0,END)
                else:
                    a = a+1
                    x.delete(0,END)
                    x.insert(END,row[a])
                        
                                             
    def Edit(self):
        selection = ProductList.curselection()[0]
        particular_id = ProductList.get(selection)
        list_of_entries = {self.entry_name,self.entry_Description,self.entry_Owner,self.entry_price}
        database.EditProducts(self.entry_name.get(),self.entry_Owner.get(),self.entry_price.get(),self.entry_Description.get(),particular_id[0])
        self.Show_product()
        




    