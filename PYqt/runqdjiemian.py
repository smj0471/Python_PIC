import sys
sys.path.append(r"./")   #导入同级目录下的文件
import PYqt.qdjiemian as qdjm


from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = qdjm.Ui_MainWindow()   #调用前端界面终端中的Ui_Dialog类
    ui.setupUi(mainWindow)  #将前端界面中的setupUi显示在创建的mainWindow中
    mainWindow.show()
    sys.exit(app.exec_())
