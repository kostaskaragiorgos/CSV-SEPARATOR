from tkinter import *
from tkinter import messagebox as msg
import csv
import pandas as pd
from tkinter import filedialog
class CSV_SEPARATOR():
    def __init__(self,master):
        self.concatlist =[]
        self.master = master
        self.master.title("CSV SEPARATOR")
        self.master.geometry("220x100")
        self.master.resizable(False,False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Exit",command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu)
        self.about_menu.add_command(label = "About",command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.master.config(menu=self.menu)
        
        self.sepfb = Button(self.master,text = "INSERT CSV FILE FOR SEPARATION"
                            ,command = self.sepfin)
        self.sepfb.pack()
        self.sepb  = Button(self.master,text = "SEPARATION",command = self.sepf)
        self.sepb.pack()
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def aboutmenu(self):
        pass
    
    def sepfin(self):
        pass
    
    def sepf(self):
        pass

        
def main():
    root=Tk()
    CS = CSV_SEPARATOR(root)
    root.mainloop()
    
if __name__=='__main__':
    main()