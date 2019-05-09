import tkinter as tk
from tkinter import messagebox





class request_admin(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self)
        self.withdraw()
        self.info = messagebox.askquestion("ask", "Do you want to accept")
        if self.info == 'yes':
            self.deiconify()

        else:
            pass

    def window(self, screen):
        self.screen = screen
        self.s = tk.Toplevel(self.screen)
        self.s.geometry('200x200')
            
    
            


