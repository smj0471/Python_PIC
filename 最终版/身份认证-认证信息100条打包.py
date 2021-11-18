# -*- coding: utf-8 -*--
import random,csv,pprint,string,json



# 要写入生成的记事本路径（deviceConfirmKey）
url_csv = r'C:/Users/liuzhao/Desktop/参数化文件.csv'
url = 'C:/Users/liuzhao/Desktop/111.txt'

taskId = '1001202101'
# 第一天第一场
gmtVerifyTime = '2021-09-01 00:00:00'
sceneId = '64099f4dabed44ab987889497bd01fd3'
subjectId = 'c536614f2259b75924e196edeb4f085c'

# 等csv文件，获取参数化数量
def csv_read(url_csv):
    with open(url_csv, 'r') as csv_reader:
        read = csv.reader(csv_reader)
        content = list(read)
        number = len(content)
        csv_reader.close()
        # 调试
        for i in content:
            print(i)
        # print(f'csv读出的：{content}')
        # print(f"csv数{number}")
    # 数据封装

    deviceConfirmKey = key()

    list_data = []
    list_date100 = []

    r_num = 3
    print("content:",len(content))




    for i in range(number):
        dict_data = {
            "deviceConfirmKey": deviceConfirmKey,
            "deviceNumber": "JYD666666",
            "examRoomId": content[i][2],
            "faceMatchScore": 88,
            "faceResult": 0,
            "fingerphoto": "",
            "fingerprintFeatures": "",
            "fingerprintMatchScore": 0,
            "fingerprintNum": 0,
            "fingerprintResult": 0,
            "gmtVerifyTime": gmtVerifyTime,
            "idCardResult": 1,
            "orgId": content[i][1],
            "rzjgid": "",
            "sceneId": sceneId,
            "scenephoto": "",
            "studentId": content[i][0],
            "subjectId": subjectId,
            "taskId": taskId,
            "taskStatus": 1,
            "temperature": "",
            "verifyResult": 1,
            "verifyType": 1
        }

        list_data.append(dict_data)
    pprint.pprint(list_data)
    for j in range(1,len(list_data),r_num): 
        list_date100.append(list_data[j:j+r_num])
    print("list_data100长度为：",len(list_date100))
    print("list_data100[0]为：",list_date100)


    # pprint.pprint(f'json_data 数据为：{json_data}')

    return list_date100


def key():
    r_num = 32
    device_confirm_key = ''.join(random.sample(string.digits + string.ascii_letters,r_num))
    return device_confirm_key
def write():
    # 将文本清空（文本初始化）
    get1 = open(url, 'w+')
    get1.seek(0)
    get1.write('')
    get1.close()

    '''写入新内容'''
    get1 = open(url, 'a+')
    get1.seek(0)

    '''要写入的内容'''
    pack_number = csv_read(url_csv)
    print("pack_number",type(pack_number))

    for m in pack_number:
        print(f'{json.dumps(m)}\n')
        get1.write(f'{json.dumps(m)}\n')   # 内容写入文本



    get1.close()

# csv_read(url_csv)

write()