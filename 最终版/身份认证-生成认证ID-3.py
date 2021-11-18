# -*- coding: utf-8 -*--
import random,csv,os,string
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
#选取参数化文件
filepath = filedialog.askopenfilename()
url_csv = filepath
print(url_csv)

#新建输出文件，要写入生成的记事本路径（deviceConfirmKey）
p,f = os.path.split(filepath)
url = p + '/deviceConfirmKey.txt'
print(url)

# 等csv文件，获取参数化数量
def csv_read(url_csv):
    with open(url_csv, 'r') as csv_reader:
        read = csv.reader(csv_reader)
        content = list(read)
        number = len(content)
    return number


def write():
    number = csv_read(url_csv) + 1

    # 将文本清空（文本初始化）

    get1 = open(url, 'w+')
    get1.seek(0)
    get1.write('')
    get1.close()

    '''写入新内容'''
    get1 = open(url, 'a+')
    get1.seek(0)

    '''要写入的内容'''
    for i in range(number):
        #生成32位数字+字母随机数
        rm_num = 32
        token = ''.join(random.sample(string.ascii_letters + string.digits,rm_num))
        get1.write(f'{token}\n')           # 内容写入文本

    get1.close()

    print(f'共生成  {number}  条deviceConfirmKey')


write()
