import base64

path = "C:\\Users\\liuzhao\\Pictures\\Camera Roll\\22.png"

#将照片转为base64码
def pic_base64(path):
    with open(path,'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = 'data:image/jpeg;base64,'+base64_data.decode()
        # print(s)
    return s

pic_base64(path)