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
        self.sepfb = Button(self.master,text = "INSERT CSV FILE FOR SEPARATION"
                            ,command = self.sepfin)
        self.sepfb.pack()
        self.sepb  = Button(self.master,text = "SEPARATION",command = self.sepf)
        self.sepb.pack()
        
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