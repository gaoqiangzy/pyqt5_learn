'''
QLineEdit综合案例

'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon           # 用来添加图标
import sys

class QLineEditDemo(QWidget) :
    def __init__(self):
        super(QLineEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLineEdit综合案例')
        formlayout = QFormLayout()  # 创建表单布局
        self.setWindowIcon(QIcon('./images/doc.ico'))

        edit1 = QLineEdit()
        # 使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)    # 设置文本框输入的最大长度
        edit1.setAlignment(Qt.AlignLeft)       # 设置左对齐
        edit1.setFont(QFont('Arial',10))        # 设置字体和字号

        # 使用浮点数校验器
        edit2=QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))     # 即表示从0.99~99.99，保留后两位

        #使用掩码校验
        edit3=QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        # 文本内容改变触发事件
        edit4=QLineEdit()
        edit4.textChanged.connect(self.textChange)

        # 设置回显的效果
        edit5=QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)      # 绑定编辑完成事件

        # 设置只读文本输入框
        edit6 = QLineEdit("Hllo Pyqt5")
        edit6.setReadOnly(True)

        formlayout.addRow("整数校验",edit1)
        formlayout.addRow("浮点数校验", edit2)
        formlayout.addRow("掩码校验", edit3)
        formlayout.addRow("文本内容改变触发事件", edit4)
        formlayout.addRow("密码回显",edit5)
        formlayout.addRow("只读文本输入框", edit6)

        self.setLayout(formlayout)

    def textChange(self):
        sender = self.sender()
        print("输入的内容："+sender.text())

    def enterPress(self):
        print("已输入值")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())
