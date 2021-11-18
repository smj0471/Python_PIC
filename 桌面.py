import os,sys
import tkinter as tk

from tkinter import *
from PIL import Image,ImageFont
from tkinter import filedialog
from tkinter import messagebox

# pic_width = 400
# pic_height = 500

#修改整个文件夹下所有照片大小
def checkfolder(width, height):

    Folderpath = filedialog.askdirectory() + '/' #获得选择好的文件夹
    Folderpath = Folderpath.replace('/','\\')
    fileName = os.listdir(Folderpath)

    for img in fileName:
        pic = Image.open(Folderpath + img)
        newpic = pic.resize((width, height),Image.ANTIALIAS)
        print (newpic)
        newpic.save(Folderpath+img)

    messagebox.showinfo("提示","照片转换完成")

#修改单个照片大小
def checkfile(width, height):

    while(1):
        filepath = filedialog.askopenfilename() #获得选择好的文件
        pic  = Image.open(filepath)
        newpic = pic.resize((width, height),Image.ANTIALIAS)
        print (newpic)
        newpic.save(filepath)

        messagebox.showinfo("提示","照片转换完成")

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

        pic_width = int(my_entry1.get())
        pic_height = int(my_entry2.get())
        print(f'长宽：{pic_width},{pic_height}')
        if pic_width == '' or pic_height == '':
            messagebox.showinfo("提示","请填写长和宽")
            print('无信息')
        else:
            radio1 = tk.Radiobutton(my_frame,text="修改单个照片",value=True,command=lambda: checkfile(int(my_entry1.get()),int(my_entry2.get())))
            radio1.grid(column=1,row=5,sticky = W)
            radio2 = tk.Radiobutton(my_frame,text="修改整个文件夹下照片",value=False,command=lambda: checkfolder(int(my_entry1.get()),int(my_entry2.get())))
            radio2.grid(column=1,row=6,sticky = W)
       
# print(pic_height,pic_width)
if __name__ == "__main__":
    MainWindow()
    