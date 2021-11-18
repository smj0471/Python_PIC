import os,sys
import tkinter as tk

from tkinter import *
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


root=Tk()
root.withdraw()
cur=filedialog.askopenfilenames(filetypes=[('all files', '.*'),('imagefiles',('.jpg','png','.jpeg'))])
if cur:
    print(cur)
else:
    print('你没有选择任何文件')