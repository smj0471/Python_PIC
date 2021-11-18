#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.Qt import *
from changepic  import *

class Example(QWidget):
    def __init__(self):
        super().__init__()  #调用父类函数
        # widget = QWidget()  #QWidget是pyqt5所有用户界面对象的基类
        self.resize(1000,800)  #设置窗口大小
        self.setWindowTitle('图片转换')  #设置窗口标题
        self.setWindowIcon(QIcon('icon.ico'))  #添加图片为窗口图标
        self.func_list()

    def func_list(self):
        self.butn()
        self.text()
        self.label()


    def butn(self):
        btn1 = QPushButton('选择单个图片（不保留原图）',self)
        btn1.resize(btn1.sizeHint())
        btn1.move(50,50)
        btn1.clicked.connect(checkfile)

        btn2 = QPushButton('选择单个图片（保留原图）',self)
        btn2.resize(btn2.sizeHint())
        btn2.move(50,100)

        btn3 = QPushButton('选择整个文件夹',self)
        btn3.resize(btn3.sizeHint())
        btn3.move(50,150)

    def text(self):
        text1 = QLineEdit(self)
        text1.move(300,50)
        text2 = QLineEdit(self)
        text2.move(300,100)

    def label(self):
        label1 = QLabel('长：',self)
        label1.move(270,50)
        label2 = QLabel('宽：',self)
        label2.move(270,100)

    def checkfile(width, height):
        if width == '' or height == '':
            QMessageBox.information("提示","请填写长和宽！")

    #修改单个照片大小,替换源文件
# def checkfile(width, height):

#     if width == '' or height =='':
#         messagebox.showinfo("提示","请填写长和宽")
#     elif int(width) < 1 or int(width) < 1 :
#         messagebox.showinfo("提示","请填写正确的长和宽！")
#     else:
#         width = int(width)
#         height = int(height)
#         while(1):
#             filepath = filedialog.askopenfilenames(filetypes=[('all files', '.*'),('imagefiles',('.jpg','png','.jpeg'))]) #获得选择好的文件
#             for img in filepath:
#                 pic  = Image.open(img)
#                 newpic = pic.resize((width, height),Image.ANTIALIAS)
#                 print (newpic)
#                 newpic.save(img)

#         messagebox.showinfo("提示","照片转换完成")


if __name__ == '__main__':
    app = QApplication(sys.argv)  #创建一个应用程序对象 
    example = Example()
    example.show()
    sys.exit(app.exec_())  #消息循环