import tkinter as tk
from tkinter import *
from tkinter import filedialog
import xlrd
from xlutils.copy import copy
import requests
from tkinter import messagebox


class MainWindow():
    def __init__(self):
        # 设置主窗口
        self.window = tk.Tk()
        self.window.minsize(500, 150)       # 设置窗口最小值
        self.window.title("获取地点坐标")

        # 添加组件
        self.addCompoents()

        # 进入消息体
        self.window.mainloop()

    def addCompoents(self):
        my_frame = tk.Frame(self.window)        # 添加一个框架，承载其他组件
        my_frame.pack(side=tk.TOP)

        # 创建单号文本:entry
        my_entry1 = tk.Entry(my_frame, bd=3, width=30)                # 边框宽度bd=5
        my_entry1.grid(column=2, row=2, sticky=W)

        my_label2 = tk.Label(my_frame, text="***Key有默认值可不输入***")
        my_label2.grid(column=1, row=1)

        my_label2 = tk.Label(my_frame, text="Key值:(高德官网的Key)")
        my_label2.grid(column=1, row=2)

        radio3 = tk.Radiobutton(my_frame, text="请选择文件", value=2,
                                command=lambda: checkfile2(my_entry1.get()))
        radio3.grid(column=1, row=7, sticky=W)


def checkfile2(key):
    url = filedialog.askopenfilename()
    # 打开第一个excel取出需要对比的内容
    excel_list = []
    a = 0
    excel = xlrd.open_workbook(url, formatting_info=True)    # 打开excel
    sheet = excel.sheets()[0]      # 读取第一个sheet页
    # 将所有信息取出存入列表
    for i in sheet.col_values(0):   # 一列
        excel_list.append(i)
    print(excel_list)

    if key == '':   # 判断是否输入了key
        key = '814af3599a23f2f3345668e9d2d653e6'

    def get_coordinate(address, key):
        parameter = {'key': key, 'address': address}
        url1 = 'https://restapi.amap.com/v3/geocode/geo?parameters'
        coordinate = requests.get(url1, params=parameter)
        try:
            coordinate.json()['geocodes'][0]['location'] != ''
        except KeyError:
            messagebox.showerror(title='提示',message='请输入正确的key值')
            checkfile2(key)
        return coordinate.json()['geocodes'][0]['location']

    coordinate_list = []
    for i in excel_list:
        coordinate = get_coordinate(i, key=key)
        coordinate_list.append(coordinate)

    excel1 = copy(excel)  # 将xlrd的对象转化为xlwt的对象
    worksheet = excel1.get_sheet('Sheet1')  # 打开第一个sheet页
    for i in range(len(coordinate_list)):
        worksheet.write(i, 2, coordinate_list[i])  # 写入内容
    excel1.save(url)  # 保存

    messagebox.showinfo('提示', '坐标获取完成！')


if __name__ == '__main__':
    MainWindow()
    pass
