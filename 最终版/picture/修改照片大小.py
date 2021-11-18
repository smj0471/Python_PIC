import os,sys
import tkinter as tk

from tkinter import *
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


#修改整个文件夹下所有照片大小
def checkfolder(width, height):

    if width == '' or height =='':
        messagebox.showinfo("提示","请填写长和宽！")
    elif int(width) < 1 or int(width) < 1 :
        messagebox.showinfo("提示","请填写正确的长和宽！")
    else:
        width = int(width)
        height = int(height)
        Folderpath = filedialog.askdirectory() + '/' #获得选择好的文件夹
        Folderpath = Folderpath.replace('/','\\')
        fileName = os.listdir(Folderpath)
        for img in fileName:
            pic = Image.open(Folderpath + img)
            newpic = pic.resize((width, height),Image.ANTIALIAS)
            print (newpic)
            newpic.save(Folderpath+img)

        messagebox.showinfo("提示","照片转换完成")

#修改单个照片大小,替换源文件
def checkfile(width, height):

    if width == '' or height =='':
        messagebox.showinfo("提示","请填写长和宽")
    elif int(width) < 1 or int(width) < 1 :
        messagebox.showinfo("提示","请填写正确的长和宽！")
    else:
        width = int(width)
        height = int(height)
        while(1):
            filepath = filedialog.askopenfilenames(filetypes=[('all files', '.*'),('imagefiles',('.jpg','png','.jpeg'))]) #获得选择好的文件
            for img in filepath:
                pic  = Image.open(img)
                newpic = pic.resize((width, height),Image.ANTIALIAS)
                print (newpic)
                newpic.save(img)

        messagebox.showinfo("提示","照片转换完成")

#修改单个照片大小，保留源文件
def checkfile2(width, height):

    if width == '' or height =='':
        messagebox.showinfo("提示","请填写长和宽")
    elif int(width) < 1 or int(width) < 1 :
        messagebox.showinfo("提示","请填写正确的长和宽！")
    else:
        width = int(width)
        height = int(height)
        while(1):
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

#修改多张照片，保留源文件


class MainWindow():
    
    def __init__(self):
        # 设置主窗口
        self.window = tk.Tk()
        self.window.minsize(500, 300)       # 设置窗口最小值
        self.window.title("修改照片大小")

        # 添加组件
        self.addCompoents()

        # 进入消息体
        self.window.mainloop()

    def addCompoents(self):
        my_frame = tk.Frame(self.window)        # 添加一个框架，承载其他组件
        my_frame.pack(side=tk.TOP)              # 布局方式，最前面/上面：top

        # def button_print():
        #     pic_width = my_entry1.get()
        #     pic_height = my_entry2.get()
        #     print(pic_width,pic_height)

        # 创建按钮：button

        # my_button = tk.Button(my_frame, text="确定",command = button_print)
        # my_button.grid(column=2,row=3)  


                

        # 创建标签：label

        my_label0 = tk.Label(my_frame, text="请填写修改后照片的大小：")
        my_label0.grid(column=1,row=0)

        my_label1 = tk.Label(my_frame, text="长")
        my_label1.grid(column=1,row=1)

        # 创建单号文本:entry
        my_entry1 = tk.Entry(my_frame, bd=4)                # 边框宽度bd=5
        my_entry1.grid(column=2,row=1,sticky = W)

        my_label2 = tk.Label(my_frame, text="宽")
        my_label2.grid(column=1,row=2)
    
        my_entry2 = tk.Entry(my_frame, bd=4)                # 边框宽度bd=5
        my_entry2.grid(column=2,row=2,sticky = W)

        my_label3 = tk.Label(my_frame, text="请选择修改类型")
        my_label3.grid(column=1,row=4,sticky = W)

        radio1 = tk.Radiobutton(my_frame,text="修改单个照片，不保留源文件（直接替换）",value=0,command=lambda: checkfile(my_entry1.get(),my_entry2.get()))
        radio1.grid(column=1,row=5,sticky = W)
        radio2 = tk.Radiobutton(my_frame,text="修改整个文件夹下照片",value=1,command=lambda: checkfolder(my_entry1.get(),my_entry2.get()))
        radio2.grid(column=1,row=6,sticky = W)
        radio3 = tk.Radiobutton(my_frame,text="修改单个照片，保留源文件",value=2,command=lambda: checkfile2(my_entry1.get(),my_entry2.get()))
        radio3.grid(column=1,row=7,sticky = W)
       

if __name__ == "__main__":
    MainWindow()
    