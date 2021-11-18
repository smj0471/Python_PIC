import tkinter as tk

from tkinter import Radiobutton

root = tk.Tk()

radio1 = Radiobutton(root,text="修改单个照片",value=True)
radio1.grid()
#checkfile()
radio2 = Radiobutton(root,text="修改整个文件夹下照片",value=False)
radio2.grid()
#checkfolder()
root.mainloop()