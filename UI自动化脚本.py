#! /usr/bin/evn python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(5)       # 查找元素等待时间，超时未查找到报错

driver.get("https://lbs.amap.com/tools/picker")   # 打开高德坐标拾取页面
"""
元素定位：
find_element_by_css_selector
driver.find_element_by_css_selector("//*[text()='文本内容']")

操作事件：
.clear()    # 清空
.click()    # 点击
.text()     # 获取文本内容
.send_keys('输入的内容')     # 输入
"""
driver.find_element_by_css_selector('#txtSearch').clear()   # 清空输入框
time.sleep(0.1)
driver.find_element_by_css_selector('#txtSearch').send_keys('竞业达')   # 输入框内写入内容
# driver.find_element_by_xpath("//*[text()='搜索']").click()        # 点击搜索
driver.find_element_by_css_selector('#myPageTop > table > tbody > tr.tr-text > td:nth-child(1) > a').click()
zb = driver.find_element_by_css_selector('#txtCoordinate').get_attribute('value')       # 复制坐标
print(zb)

driver.quit()  # 关闭浏览器