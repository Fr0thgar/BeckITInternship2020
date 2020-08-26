

#Dette er test kode i forbindelse med betalings metode research

from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Customer:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Test")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

if __name__ == "__main__":
    root =  Tk()
    application = Customer (root)
    root.mainloop()

       
