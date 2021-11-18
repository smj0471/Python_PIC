#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser,os

# path = 'D:/Python文件夹/config.ini'
# cf = configparser.ConfigParser()
# a = cf.read(path)
# stnum = a["stnum"]
# print(stnum)




 
 
# ########函数############
 
conf = configparser.ConfigParser()
 
a = conf.read("config.ini")
print("config.inf = ", a) 
 
print (conf.items("oppo"))
 
secs = conf.sections()
print ("secs=", secs)
 
options = conf.options("mysql")
print ("options=", options)
 
items = conf.items("mysql")
print ("items=", items)
 
host = conf.get("mysql","host")
print ("host=",host)