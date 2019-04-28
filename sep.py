from tkinter import *
from tkinter import messagebox as msg
#import csv
import os 
import pandas as pd
from tkinter import filedialog
class CSV_SEPARATOR():
    def __init__(self,master):
        self.concatlist =[]
        self.master = master
        self.master.title("CSV SEPARATOR")
        self.master.geometry("270x100")
        self.master.resizable(False,False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator= 'Alt+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
        self.sepfb = Button(self.master,text = "INSERT CSV FILE FOR SEPARATION"
                            ,command = self.sepfin)
        self.sepfb.pack()
    
    def helpmenu(self):
        msg.showinfo("Help","HOW TO USE THIS APP \n 1. Insert a .csv file \n 2.Insert the number of files your csv is going to be serarated \n 3.Press the SEPARATION button")
    
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def aboutmenu(self):
        msg.showinfo("About SEPARATOR","Version 0.1\nSeparates your csv files")
    
    def sepfin(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        if ".csv" in self.filename:
            self.sepfb.configure(state="disable")
            self.pandascheck = pd.read_csv(self.filename)
            self.indexs = Label(self.master,text = "INDEX:"+str(self.pandascheck.index.size))
            self.indexs.pack()
            self.howtosep = Label(self.master,text = "How many files you need for separation")
            self.howtosep.pack()
            self.texttosep = Text(self.master,height = 1 , width =3 )
            self.texttosep.pack()
            self.sepb  = Button(self.master,text = "SEPARATION",command = self.sepf)
            self.sepb.pack()
        else:
            msg.showerror("ERROR","NO FILE INSERTED \n INSERT A CSV FILE ")
    
    def sepf(self):
        try:
            int(self.texttosep.get(1.0,END))
        except:
            self.texttosep.delete(1.0,END)
            msg.showerror("ERROR","YOU HAVE TO ENTER A NUMMBER OR AN INTEGER")
        else:
            if int(self.texttosep.get(1.0,END)) > 0:
                if int(self.pandascheck.index.size) <= int(self.texttosep.get(1.0,END)):
                    msg.showerror("ERROR","THE NUMBER OF FILES YOU WANT TO SEPARATE THE CSV MUST ME SMALLER THAN THE CSV'S INDEX")
                else:
                    print("separation can be done")
                    self. i = 1 
                    self.name = str("separate") + str(self.i)
                    while os.path.exists(self.name) == True:
                        self.i = self.i+1
                        self.name = str("separate") + str(self.i)
                    os.mkdir(self.name)
                    os.chdir(self.name)
                    """
                    self.indexsaverange = int(self.texttosep.get(1.0,END))/(int(self.pandascheck.index.size)-1)
                    while int(self.texttosep.get(1.0,END))>0:
                        self.pandascheck = pd.read_csv(self.filename)
                        for i in range(int(self.indexsaverange)):
                            print(self.pandascheck[i])
                    """
                    
                    
            else:
                self.texttosep.delete(1.0,END)
                msg.showerror("ERROR","YOU HAVE TO ENTER A POSITIVE NUMBER OR BIGGER THAN ZERO")
                
            
        
def main():
    root=Tk()
    CS = CSV_SEPARATOR(root)
    root.mainloop()
    
if __name__=='__main__':
    main()