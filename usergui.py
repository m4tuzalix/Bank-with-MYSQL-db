from tkinter import *
from tkinter import messagebox
import database
from collections import OrderedDict
from PIL import ImageTk, Image
from orders import buy



class gui2(Toplevel):
    def __init__(self, master, nick):
        self.nick=nick
        Toplevel.__init__(self,master)
        Tk.title(self,'managament app')
        Tk.geometry(self,'970x600+0+0')
        Tk.configure(self, bg='blue')

        #containers for data
        self.prodName = StringVar()
        self.prodOwner = StringVar()
        self.prodPrice = StringVar()
        self.prodDescription = StringVar()
        
        

    
        #frames
        Main = Frame(self, bg='green', bd=1)
        Main.grid()
        

        Header = Frame(Main, bg='green', bd=1, padx=54, pady=8, relief=RIDGE) #////// title space
        Header.pack(side=TOP)

        self.Header_text = Label(Header, font=('times new roman', 40, 'bold'), text="managament", bg='green')
        self.Header_text.grid()

        ClickFrame = Frame(Main, bd=1, width=1350, height=70, padx=18, pady=10, bg='green', relief=RIDGE) #//// buttons space
        ClickFrame.pack(side=BOTTOM)

        Data = Frame(Main, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg='green') #////// content space
        Data.pack(side=BOTTOM)

        DataLeft = LabelFrame(Data, bd=1, width=1000, height=800, padx=20, pady=10, relief=RIDGE, bg='green', text='Product information\n', font=('arial', 20, 'bold'))
        DataLeft.pack(side=LEFT)

        DataRight = LabelFrame(Data, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg='green',  text='Product details\n', font=('arial', 20, 'bold'))
        DataRight.pack(side=RIGHT)

        ##entries and labels

        self.productName = Label(DataLeft, text='Product name')
        self.productName.grid(row=1, column=0, sticky=W)
        self.entry_name = Entry(DataLeft, textvariable=self.prodName, width=39)
        self.entry_name.grid(row=1, column=1)

        self.productPrice = Label(DataLeft, text='Product owner')
        self.productPrice.grid(row=2, column=0, sticky=W)
        self.entry_price = Entry(DataLeft, textvariable=self.prodPrice, width=39)
        self.entry_price.grid(row=2, column=1)

        self.productOwner = Label(DataLeft, text='Product price')
        self.productOwner.grid(row=3, column=0, sticky=W)
        self.entry_Owner = Entry(DataLeft, textvariable=self.prodOwner, width=39)
        self.entry_Owner.grid(row=3, column=1)

        self.productDescription = Label(DataLeft, text='Product description')
        self.productDescription.grid(row=4, column=0, sticky=W)
        self.entry_Description = Entry(DataLeft, textvariable=self.prodDescription, width=39)
        self.entry_Description.grid(row=4, column=1)

        self.search = Label(DataLeft, text='Search')
        self.search.grid(row=5,column=0, sticky=W)
        self.entry_Search = Entry(DataLeft, width=50)
        self.entry_Search.grid(row=5, column=1)

        
        
        
        ### labels editing loop
        global test
        test = {self.productDescription,
        self.productOwner, self.productPrice, self.productName, self.search}
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

        self.buttonBuy = Button(ClickFrame, text='Buy', command=self.buy)
        self.buttonBuy.grid(row=0, column=0)

        self.buttonSell = Button(ClickFrame, text='Sell')
        self.buttonSell.grid(row=0, column=1)

        self.buttonSearch = Button(ClickFrame, text='Search', command=self.Search_item)
        self.buttonSearch.grid(row=0, column=2)

        self.buttonRefresh = Button(ClickFrame, text='Refresh', command=self.Refresh)
        self.buttonRefresh.grid(row=0, column=4)

        test2 = {self.buttonBuy, self.buttonSell, self.buttonSearch, self.buttonRefresh}
        for z in test2:
            z.configure(width=10, height=1, bd=4, font=('times new roman', 20, 'bold'))

        

    
        ProductList.delete(0,END)
        for row in database.ViewProducts():
            ProductList.insert(END, row)
    
    def Refresh(self):
        ProductList.delete(0,END)
        for row in database.ViewProducts():
            ProductList.insert(END, row)

    def Search_item(self):
        ProductList.delete(0,END)
        for row in database.SearchProducts(self.entry_Search.get(),ProductList):
            ProductList.insert(END,row)
        
    def ChooseProduct(self,Event=None):
        a = 0
        selection = ProductList.curselection()[0]
        particular_id = ProductList.get(selection)
        list_of_entries = {self.entry_Owner:2,self.entry_price:3,self.entry_name:1,self.entry_Description:4}
        for x in OrderedDict(sorted(list_of_entries.items(), key=lambda t:t[1])):
            if len(particular_id)==0:
                x.delete(0,END)
            else:
                for p in range(1):
                    a = a+1
                    x.delete(0,END)
                    x.insert(END,particular_id[a])
            

    def buy(self):
        buy(self.nick,self.entry_name.get())
                    
            
            