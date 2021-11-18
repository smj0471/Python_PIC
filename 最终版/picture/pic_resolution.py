#修改照片分辨率

import os
from PIL import Image

path = 'C:\\Users\\liuzhao\\Pictures\\Camera Roll\\22.png'

#获取照片内存大小
def ima_Size(path):
    imagePath = os.path.join(path)
    imageSize = os.path.getsize(imagePath)
    imageSize /= 1024 # 除以1024是代表Kb
    # print(imageSize)
    return imageSize


def ima_pixmap(path):
    image = Image.open(path)
    imagePixmap = Image.size	# 宽高像素
    print(imagePixmap)

ima_pixmap(path)
