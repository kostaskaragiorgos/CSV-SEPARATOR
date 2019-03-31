from tkinter import *
from tkinter import messagebox as msg
#import csv
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
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def aboutmenu(self):
        msg.showinfo("About SEPARATOR","Separates your csv files")
    
    def sepfin(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        if ".csv" in self.filename:
            print(self.filename)
            self.sepfb.configure(state="disable")
            self.howtosep = Label(self.master,text = "How many files you need for separation")
            self.howtosep.pack()
            self.texttosep = Text(self.master,height = 1 , width =3 )
            self.texttosep.pack()
            self.sepb  = Button(self.master,text = "SEPARATION",command = self.sepf)
            self.sepb.pack()
        
            self.pandascheck = pd.read_csv(self.filename)
            print(str(self.pandascheck.index.size))
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
                    """
                    TODO
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