from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from tkinter import filedialog
import xlrd
from xlutils.copy import copy
import base64
import json
import requests


password = 'jydadminjydadmin' #秘钥



#读取文件中需要加密的原文
excel_list = []
url = filedialog.askopenfilename()
excel = xlrd.open_workbook(url,formatting_info=True)#打开Excel表格
sheet = excel.sheets()[0]#读取第一个sheet页
for i in sheet.col_values(0):
    excel_list.append(i)
print(excel_list)

#加密
class EncryptDate:
    def __init__(self, key):
        self.key = key.encode("utf-8")  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)

eg = EncryptDate(password)  # 这里密钥的长度必须是16的倍数
# data = 370000
# res = eg.encrypt(str(data))
# print(res)
#输出解密信息
# print(eg.decrypt(res))



encrypt_list = []
for i in excel_list:
    print("i is :",i)
    encrypt = eg.encrypt(str(i))
    print('encrypt is :',encrypt)
    encrypt_list.append(encrypt)

#将加密后的内容写入Excel表中
excel_write = copy(excel) #复制一份之前的Excel表格开启写入模式
worksheet = excel_write.get_sheet('Sheet1')
for i in range(len(encrypt_list)):
    worksheet.write(i,2,encrypt_list[i])
excel_write.save(url) #保存表格


