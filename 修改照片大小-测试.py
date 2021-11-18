import os,sys
import tkinter as tk

from PIL import Image
from tkinter import filedialog
from tkinter import messagebox

width = 400
height = 500


def checkfolder():

    Folderpath = filedialog.askdirectory() + '/' #获得选择好的文件夹
    Folderpath = Folderpath.replace('/','\\')
    fileName = os.listdir(Folderpath)

    for img in fileName:

        pic = Image.open(Folderpath + img)

        newpic = pic.resize((width, height),Image.ANTIALIAS)

        print (newpic)

        newpic.save(Folderpath+img)

def checkfile():

    while(1):


        filepath = filedialog.askopenfilename() #获得选择好的文件

        pic  = Image.open(filepath)

        newpic = pic.resize((width, height),Image.ANTIALIAS)

        print (newpic)

        newpic.save(filepath)

def checkfile111():

    while(1):

        filepath = filedialog.askopenfilename() #获得选择好的文件

        pic  = Image.open(filepath)

        newpic = pic.resize((width, height),Image.ANTIALIAS)

        print (newpic)

        newpic.save(filepath)

checkfile111()

messagebox.showinfo("提示","照片转换完成")