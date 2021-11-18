# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.withdraw()
# filepath = filedialog.askopenfilename()

# print(filepath)
        

# import random
# import string

# # 指定随机数长度
# r_num = 4

# # 生成数字 + 字母（字符串序列）
# token = string.ascii_letters + string.digits
# '''
#     string.ascii_letters:生成大小写字母（type:字符串）
#     string.digits:生成数字（type:字符串）
# '''

# # 随机选择 指定长度 随机码（字符串列表）
# token = random.sample(token,r_num)

# # 生成 数字 + 字母 随机数
# token = ''.join(token)

# # 加强版（一行代码）
# token = ''.join(random.sample(string.digits + string.ascii_letters,r_num))


#列表取固定数量值

# list = [1,2,3,4,5,6,7,8,9]  # csv数

# ret = []
# for i in range(0,len(list), 2):
#     ret.append(list[i:i+2])
#     print(list[i:i+2])



import base64
import io
import os
from PIL import Image
from PIL import ImageFile
 
# 压缩图片文件
def compress_image(outfile, mb, quality, k):
    """不改变图片尺寸压缩到指定大小
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
 
    o_size = os.path.getsize(outfile) // 1024
    print(o_size, mb)
    if o_size <= mb:
        return outfile
    
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    while o_size > mb:
        im = Image.open(outfile)
        x, y = im.size
        out = im.resize((int(x*k), int(y*k)), Image.ANTIALIAS)
        try:
            out.save(outfile, quality=quality)
        except Exception as e:
            print(e)
            break
        o_size = os.path.getsize(outfile) // 1024
    return outfile
 
# 压缩base64的图片
def compress_image_bs4(b64, mb=190, k=0.9):
    """不改变图片尺寸压缩到指定大小
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    f = base64.b64decode(b64)
    with io.BytesIO(f) as im:
        o_size = len(im.getvalue()) // 1024
        if o_size <= mb:
            return b64
        im_out = im
        while o_size > mb:
            img = Image.open(im_out)
            x, y = img.size
            out = img.resize((int(x*k), int(y*k)), Image.ANTIALIAS)
            im_out.close()
            im_out = io.BytesIO()
            out.save(im_out, 'jpeg')
            o_size = len(im_out.getvalue()) // 1024
        b64 = base64.b64encode(im_out.getvalue())
        im_out.close()
        return str(b64, encoding='utf8')

compress_image('C:\\Users\\liuzhao\\Pictures\\Camera Roll\\22.png',100, 85, 0.9)