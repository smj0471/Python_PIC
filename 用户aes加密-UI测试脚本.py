from selenium import webdriver
import time
import xlrd
import pprint
import os
from xlutils.copy import copy


def AES_encryption(list1):
    dict1 = {}
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_work_dir = current_dir + '/chromedriver.exe'
    driver = webdriver.Chrome(current_work_dir)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://tool.chacuo.net/cryptaes")

    time.sleep(2)

    driver.find_element_by_css_selector('#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > select:nth-child(4)').click()
    driver.find_element_by_css_selector('#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > select:nth-child(4) > option:nth-child(1)').click()

    driver.find_element_by_css_selector('#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > input:nth-child(8)').clear()
    driver.find_element_by_css_selector('#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > input:nth-child(8)').send_keys('jydadminjydadmin')

    for i in list1:
        time.sleep(1)
        driver.find_element_by_css_selector('#converts').clear()
        time.sleep(0.5)
        driver.find_element_by_css_selector('#converts').send_keys(i)

        time.sleep(1)
        driver.find_element_by_css_selector('#main > div.middle > div > div.convert.alert-info.alert > div.tc > input:nth-child(1)').click()

        time.sleep(0.5)
        result = driver.find_element_by_css_selector('#convertd').get_attribute('value')

        if result == '请不要这么快提交，稍后再试！':
            time.sleep(2)
            driver.refresh()    # 刷新页面
            time.sleep(15)
            driver.find_element_by_css_selector(
                '#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > select:nth-child(4)').click()
            driver.find_element_by_css_selector(
                '#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > select:nth-child(4) > option:nth-child(1)').click()

            time.sleep(1)
            driver.find_element_by_css_selector(
                '#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > input:nth-child(8)').clear()
            driver.find_element_by_css_selector(
                '#main > div.middle > div > div.convert.alert-info.alert > div:nth-child(1) > input:nth-child(8)').send_keys(
                'jydadminjydadmin')
            continue

        # print(result)
        dict1.update({i: result})
        # print(dict1)
        print(f'{i}:{result}')

    driver.quit()
    return dict1


url_excle = 'C:/Users/liuzhao/Desktop/登录账号.xls'


# 在excel内读取信息，输入读取信心的所在列数（A是第0列，B是第1列，C是第2列）
def read_excel(column, url=url_excle):
    excel_list = []
    excel = xlrd.open_workbook(url, formatting_info=True)    # 打开excel
    sheet = excel.sheets()[0]      # 打开第一个sheet页
    # 将所有信息取出存入列表
    for i in sheet.col_values(column):   # 一列
        excel_list.append(i)
    return excel_list


# 在excel内写入信息，输入要写入信息的所在列数（A是第0列，B是第1列，C是第2列）
def write_excel(dict, column, url=url_excle):
    excel = xlrd.open_workbook(url, formatting_info=True)  # 打开excel
    excel1 = copy(excel)  # 将xlrd的对象转化为xlwt的对象
    worksheet = excel1.get_sheet('Sheet1')  # 打开第一个sheet页
    for i in range(len(list(dict.keys()))):
        worksheet.write(i, column, list(dict.keys())[i])  # 写入地址名称
        worksheet.write(i, column+1, dict[list(dict.keys())[i]])  # 写入地址坐标
    excel1.save(url)  # 保存


if __name__ == '__main__':
    list_excel = read_excel(0)
    dict_UI = AES_encryption(list_excel)
    pprint.pprint(dict_UI)
    write_excel(dict_UI, 1)
    pass
