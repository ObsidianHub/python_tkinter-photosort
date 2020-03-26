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
root.geometry('500x150+1000+300')

frame = Frame(root, bg="#56ADFF", bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = Button(frame, text="Выбрать папку", command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = Button(root, text="Start", command=f_start)
btn_start.pack(fill=X, padx=10)

root.mainloop()