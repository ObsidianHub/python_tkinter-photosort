from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from datetime import datetime

def choose_dir():
  pass

def f_start():
  pass

root = Tk()
root.title('PhotoSort')
root.geometry('500x150')

frame = Frame(root, bg="#56ADFF")
frame.pack()

e_path = Entry(frame)
e_path.pack(side=LEFT, expand=True, fill=X)

root.mainloop()