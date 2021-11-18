import sys
from PyQt5 import QtCore
sys.path.append(r"./")   #导入同级目录下的文件
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('工具箱')  #设置主窗口标题
        self.resize(1000,800)  #设置窗口尺寸
        self.setWindowIcon(QIcon('./image/toolbox.ico'))  #设置窗口图标
        # self.status = self.statusBar()  #状态栏
        # self.status.showMessage('XXXXX',5000)

        #label控件
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color = red>这是一个标签</font>")
        label1.setAutoFillBackground(True)  #自动填充背景
        palette = QPalette()  #创建一个调色板
        palette.setColor(QPalette.Window,Qt.blue)  #设置背景色
        label1.setPalette(palette)   #对label使用调色板
        label1.setAlignment(Qt.AlignHCenter)  #设置文本居中对齐

        label2.setText("<a href = '#'>欢迎</a>")

        label3.setAlignment(Qt.AlignHCenter)
        label3.setToolTip('图片')
        label3.setPixmap(QPixmap('./image/5.png'))
        label3.setScaledContents(True)

        # label4.openExternalLinks(True) #设置打开连接,打开连接和触发事件是互斥的，只能二者选其一
        label4.setText("<a href = 'http://www.baidu.com'>百度一下</a>")
        label4.setAlignment( Qt.AlignHCenter)
        label4.setToolTip('这是一个超链接')

        #垂直布局
        #QMainWindow框架下，所有的布局不会有效果，需要添加一下4行才可以正常使用布局
        widget = QWidget()
        vbox = QVBoxLayout(self)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)


    def linkHovered(self):
        print('鼠标滑过事件')

    def linkClicked(self):
        print('鼠标单击事件')


    #设置窗口居中显示
    def center(self):
        screen = QDesktopWidget().screenGeometry()  #获取屏幕坐标
        size = self.geometry()  #获取窗口坐标系
        newleft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newleft,newTop)

#创建label的伙伴关系
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

        vgrid = QGridLayout(self)
        vgrid.addWidget(nameLable,0,0)
        vgrid.addWidget(nameLineEdit,0,1,1,2)
        vgrid.addWidget(passwordLable,1,0)
        vgrid.addWidget(passwordLineEdit,1,1,1,2)
        vgrid.addWidget(okbun,2,0)
        vgrid.addWidget(cancelbun,2,2)

#QLineEdit控件与回显模式
'''
4种回显模式
Normal：正常输入回显
NoEcho：不回显
Password：密码回显
PasswordEchoOnEdit：输入的时候显示明文，切换到其他控件时显示密文
'''
class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        PasswordEchoOnEditLineEdit = QLineEdit()

        formLate = QFormLayout()
        formLate.addRow("Normal",normalLineEdit)
        formLate.addRow("NoEcho", noEchoLineEdit)
        formLate.addRow("Password", passwordLineEdit)
        formLate.addRow("PasswordEchoOnEdit", PasswordEchoOnEditLineEdit)

        #setPlaceholderText默认提示
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        PasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        PasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.setLayout(formLate)

#QLineEdit空间输入（校验器）
class QLineEditValidater(QWidget):
    def __init__(self):
        super(QLineEditValidater, self).__init__()
        self.initUI()

    def initUI(self):
        formlayou = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()
        maskLineEdit = QLineEdit()

        formlayou.addRow(intLineEdit)
        formlayou.addRow(doubleLineEdit)
        formlayou.addRow(validatorLineEdit)
        formlayou.addRow(maskLineEdit)

        intLineEdit.setPlaceholderText("整型")
        doubleLineEdit.setPlaceholderText("浮点型")
        validatorLineEdit.setPlaceholderText("字母和数字")
        maskLineEdit.setInputMask('AAAA-AAAA-AAAA-AAAA;#')  #输入固定格式的内容，没输入时#代替

        #整数校验器（1,99）
        intvalidator = QIntValidator(self)
        intvalidator.setRange(1,99)

        #浮点校验器（-300,300） 小数点后2位
        doublevalidator = QDoubleValidator(self)
        doublevalidator.setRange(-300,300)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation)
        #设置精度，小数点2位
        doublevalidator.setDecimals(2)

        #字符和数字校验器
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器
        intLineEdit.setValidator(intvalidator)
        doubleLineEdit.setValidator(doublevalidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formlayou)

'''
QTestEdit控件
'''
class QTestEditDome(QWidget):
    def __init__(self):
        super(QTestEditDome, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,280)
        self.textEdit = QTextEdit()
        self.buttonText = QPushButton()
        self.buttonHTML = QPushButton()
        self.buttonToEdit =QPushButton()
        self.buttonToHTML = QPushButton()

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToEdit)
        layout.addWidget(self.buttonToHTML)
        self.setLayout(layout)

        self.buttonText.clicked.connect(self.clickButtonText)
        self.buttonHTML.clicked.connect(self.clichedbuttonHTML)
        self.buttonToEdit.clicked.connect(self.clickButtonToText)
        self.buttonToHTML.clicked.connect(self.clickButtonToHTML)

    #文本框显示输入内容
    def clickButtonText(self):
        self.textEdit.setPlainText('XXXX')

    #设置文本框格式
    def clichedbuttonHTML(self):
        self.textEdit.setHtml('<font color = "red" size = "6">CCC</font>')

    #获取文本框内容
    def clickButtonToText(self):
        print(self.textEdit.toPlainText())

    #获取文本框HTML信息
    def clickButtonToHTML(self):
        print(self.textEdit.toHtml())

'''
button按钮
'''
class QPushButtonDemo(QWidget):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.button1 = QPushButton()
        self.button1.setText("first")
        self.button1.setCheckable(True)  #和toggle方法是配套使用的
        self.button1.toggle()  #开关按钮
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))  #lambda表示方法或槽，调用函数
        self.button1.clicked.connect(self.buttonState)

        #文本前显示图片
        self.button2 = QPushButton()
        self.button2.setIcon(QIcon(QPixmap('./image/2.jpg')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))

        #不可用的按钮
        self.button3 = QPushButton()
        self.button3.setEnabled(False)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setLayout(layout)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮被选中')
        else:
            print('按钮未被选中')

    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() +'>')

'''
单选按钮控件(QRedioButton)
'''
class QRedioButtonDemo(QWidget):
    def __init__(self):
        super(QRedioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.redioButton1 = QRadioButton('按钮1')
        self.redioButton1.setCheckable(True)
        self.redioButton2 = QRadioButton('按钮2')
        self.redioButton2.setCheckable(True)
        self.redioButton1.toggled.connect(self.clickedRedioButton)   #状态切换的方法
        self.redioButton2.toggled.connect(self.clickedRedioButton)
        layout.addWidget(self.redioButton1)
        layout.addWidget(self.redioButton2)
        self.setLayout(layout)

    def clickedRedioButton(self):
        rediobutton = self.sender() #获取当前点击的按钮
        if rediobutton.text() == '按钮1':
            if rediobutton.isChecked() == True:
                print('<' + rediobutton.text() + '>被选中')
            else:
                print('<' + rediobutton.text() + '>未被选中')
        if rediobutton.text() == '按钮2':
            if rediobutton.isChecked() == True:
                print('<' + rediobutton.text() + '>被选中')
            else:
                print('<' + rediobutton.text() + '>未被选中')

'''
复选框QCheckBox
3中状态：
未选中：0
半选中：1
选中：2
'''
class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        self.checkbox1 = QCheckBox('复选框1')
        self.checkbox1.setCheckable(True)
        self.checkbox1.stateChanged.connect(lambda :self.checkedcheckbox(self.checkbox1))
        self.checkbox2 = QCheckBox('复选框2')
        self.checkbox2.setCheckable(True)
        self.checkbox2.stateChanged.connect(lambda: self.checkedcheckbox(self.checkbox2))
        self.checkbox3 = QCheckBox('半选框')
        self.checkbox3.stateChanged.connect(lambda :self.checkedcheckbox(self.checkbox3))
        self.checkbox3.setTristate(True)   #这两个是半选框必须要设置的属性
        self.checkbox3.setCheckState(Qt.PartiallyChecked)  #这两个是半选框必须要设置的属性
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.checkbox3)
        self.setLayout(layout)

    def checkedcheckbox(self,cb):
        check1State = self.checkbox1.text() + ', isChecked=' + str(self.checkbox1.isChecked()) + ', checkState=' + str(self.checkbox1.checkState()) + '\n'
        check2State = self.checkbox2.text() + ', isChecked=' + str(self.checkbox2.isChecked()) + ', checkState=' + str(self.checkbox2.checkState()) + '\n'
        check3State = self.checkbox3.text() + ', isChecked=' + str(self.checkbox3.isChecked()) + ', checkState=' + str(self.checkbox3.checkState()) + '\n'
        print(check1State + check2State + check3State)



if __name__ == '__main__':
    
    app = QApplication(sys.argv)  # 创建一个QApplication的实例

    # main = MainWindow()
    # main = QlabelBuddy()
    # main = QLineEditEchoMode()
    # main = QLineEditValidater()
    # main = QTestEditDome()
    # main = QPushButtonDemo()
    # main = QRedioButtonDemo()
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_()) #进入系统循环