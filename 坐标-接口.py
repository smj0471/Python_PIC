import tkinter as tk
from tkinter import *
from tkinter import filedialog
import xlrd
from xlutils.copy import copy
import requests
from tkinter import messagebox
# 我的key = 814af3599a23f2f3345668e9d2d653e6

key = '814af3599a23f2f3345668e9d2d653e6'


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
        my_frame.pack(side=tk.TOP) 

        my_label2 = tk.Label(my_frame, text="key值:")
        my_label2.grid(column=0,row=4,sticky = W) 

        # 创建单号文本:entry
        my_entry1 = tk.Entry(my_frame, bd=4)                # 边框宽度bd=5
        my_entry1.grid(column=1,row=4,sticky = W)

        my_label1 = tk.Label(my_frame, text="是否有高德地图官网申请Web服务API类型Key？")
        my_label1.grid(column=0,row=1,COMMAND=my_entry1.grid_forget()) 

        

        radio1 = tk.Radiobutton(my_frame,text="没有，使用系统默认key值",value=True,command=lambda: get_schoolname(key))
        radio1.grid(column=0,row=2,sticky = W)
        radio2 = tk.Radiobutton(my_frame,text="有，使用自己的key值",value=False,command=lambda: get_schoolname(my_entry1.get()))
        radio2.grid(column=0,row=3,sticky = W,COMMAND=my_entry1.grid())

        

def get_schoolname(key):
    url = filedialog.askopenfilename()

    # 打开第一个excel取出需要对比的内容
    excel_list = []
    excel = xlrd.open_workbook(url, formatting_info=True)    # 打开excel
    sheet = excel.sheets()[0]      # 读取第一个sheet页
    # 将所有信息取出存入列表
    for i in sheet.col_values(0):   # 一列
        excel_list.append(i)
    print(excel_list)

    def get_coordinate(address, key):
        parameter = {'key': key, 'address': address}
        url1 = 'https://restapi.amap.com/v3/geocode/geo?parameters'
        coordinate = requests.get(url1, params=parameter)
        # print(f"{coordinate.json()['geocodes'][0]['location']}")

        try:
            coordinate.json()['geocodes'][0]['location'] != ''
        except KeyError:
            messagebox.showerror(title='提示',message='请输入正确的key值')
            get_schoolname(key)

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
    messagebox.showinfo('提示','坐标获取完成！')



if __name__ == '__main__':
    MainWindow()
    pass

