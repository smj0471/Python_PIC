import sys
from PyQt5.QtWidgets import *

class QlabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        nameLable = QLabel('&Name',self)   #创建热键
        nameLineEdit = QLineEdit(self)  
        nameLable.setBuddy(nameLineEdit)  #创建伙伴关系

        passwordLable = QLabel('&Password',self)   #创建热键
        passwordLineEdit = QLineEdit(self)  
        passwordLable.setBuddy(passwordLineEdit)  #创建伙伴关系

        okbun = QPushButton('&OK')
        cancelbun = QPushButton('&Cancel')

        # widget = QWidget()
        vgrid = QGridLayout(self)
        # widget.setLayout(vgrid)

        vgrid.addWidget(nameLable,0,0)
        vgrid.addWidget(nameLineEdit,0,1,1,2)
        vgrid.addWidget(passwordLable,1,0)
        vgrid.addWidget(passwordLineEdit,1,1,1,2)
        vgrid.addWidget(okbun,2,0)
        vgrid.addWidget(cancelbun,2,2)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)  # 创建一个QApplication的实例

    main = QlabelBuddy()
    main.show()
    sys.exit(app.exec_()) #进入系统循环