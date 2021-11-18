import os,sys
import tkinter as tk

from tkinter import *
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


root=Tk()
root.withdraw()
# cur=filedialog.askopenfilenames(filetypes=[('all files', '.*'),('imagefiles',('.jpg','png','.jpeg'))])
# if cur:
#     print(cur)
# else:
#     print('你没有选择任何文件')




def checkfolder(width, height):

    if width == '' or height =='':
        messagebox.showinfo("提示","请填写长和宽！")
    elif int(width) < 1 or int(width) < 1 :
        messagebox.showinfo("提示","请填写正确的长和宽！")
    else:
        width = int(width)
        height = int(height)

        filepath = filedialog.askopenfilenames(filetypes=[('all files', '.*'),('imagefiles',('.jpg','png','.jpeg'))])
        
        for img in filepath:
            pic  = Image.open(img)
            newpic = pic.resize((width, height),Image.ANTIALIAS)
            print (newpic)

            p,f = os.path.split(img)
            print ( " dir is: " + p)
            print ( " file is: " + f)
            newfilepath = p + "/newfile/" 
            if not os.path.exists(newfilepath):
                os.makedirs(newfilepath)

            newpic.save(newfilepath + f)

        messagebox.showinfo("提示","照片转换完成")

checkfolder(200,300)