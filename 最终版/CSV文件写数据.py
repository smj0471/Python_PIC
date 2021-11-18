#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入CSV安装包
import csv


# 1. 创建文件对象
f = open('GKXCB.csv','w',encoding='utf-8',newline='')

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

# 3. 构建列表头
# csv_writer.writerow(['ksh','xm','sfzh','lxdh','yxdh','yxmc','kldm','zydh','zymc','pcdm'])
csv_writer.writerow(['Ksh','Xm','Sfzh4','Lxdh4','CXBZ','Tkkmdm','Xkkmzhdm','Km1','Km2','Km3','Km4','Km5','Km6','Km7','Km8','Km9','Zf','TZF','Wc','Wc04','Wc05','Wc06','Wc07','Wc08','Wc09','Bz','km1wjbz','km2wjbz','km3wjbz','km4wjbz','km5wjbz','km6wjbz','km7wjbz','km8wjbz','km9wjbz'])

# 4. 写入csv文件内容
for i in range(1,50000):
    ksh = 21376666000001 + i
    xm = "WANG" + str(i)
    csv_writer.writerow([ksh,xm,'1234','4321','1','1','04','104','102','120','75','63','68','','','','532','5','72317','49186','52641','49383','','','','29253','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL'])


# 5. 关闭文件
f.close()
