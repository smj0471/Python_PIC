from selenium import webdriver
import time,os
import xlrd
import pprint
from xlutils.copy import copy
from tkinter import filedialog


url_excle = filedialog.askopenfilename()

# url_excle = 'C:/Users/jwl/Desktop/111.xls'

# driver = webdriver.Chrome('C:/Users/liuzhao/Desktop/chromedriver_win32/chromedriver.exe')
#获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
current_work_dir = current_dir + '/chromedriver.exe'
driver = webdriver.Chrome(current_work_dir)

driver.implicitly_wait(8)       # 查找元素等待时间，超时未查找到报错
driver.get("http://tool.chacuo.net/cryptaes/")   # 打开高德坐标拾取页面


# UI获取地点坐标
def get_coordinates(location):
    time.sleep(5)
    dict = {}
    for i in location:
        driver.find_element_by_id('converts').clear()      # 清空输入框
        time.sleep(0.1)
        driver.find_element_by_id('converts').send_keys(i)   # 输入框内写入内容
        driver.find_element_by_id('{"minlength":1}').send_key
        driver.find_element_by_class_name('btn f14 h30').click()        # 点击搜索
        time.sleep(0.1)
        coordinates = driver.find_element_by_id('convertd').get_attribute('value')       # 复制坐标
        dict.update({i: coordinates})
    return dict


# 在excel内读取地点信息，输入读取地点的所在列数（A是第0列，B是第1列，C是第2列）
def read_excel(column, url=url_excle):
    excel_list = []
    excel = xlrd.open_workbook(url, formatting_info=True)    # 打开excel
    sheet = excel.sheets()[0]      # 打开第一个sheet页
    # 将所有信息取出存入列表
    for i in sheet.col_values(column):   # 一列
        excel_list.append(i)
    return excel_list


# 在excel内写入地点和经纬度信息，输入要写入地点的所在列数（A是第0列，B是第1列，C是第2列）
def write_excel(dict, column, url=url_excle):
    excel = xlrd.open_workbook(url, formatting_info=True)  # 打开excel
    excel1 = copy(excel)  # 将xlrd的对象转化为xlwt的对象
    worksheet = excel1.get_sheet('Sheet1')  # 打开第一个sheet页
    for i in range(len(list(dict.keys()))):
        worksheet.write(i, column, list(dict.keys())[i])  # 写入地址名称
        worksheet.write(i, column+1, dict[list(dict.keys())[i]])  # 写入地址坐标
    excel1.save(url)  # 保存


if __name__ == '__main__':
    list1 = read_excel(0)    # 读出excel表内地址。输入地址所在列
    dict1 = get_coordinates(list1)  # UI获取地点坐标
    pprint.pprint(dict1)
    write_excel(dict1, 2)      # 地点坐标写入原表

    # driver.quit()  # 关闭浏览器
