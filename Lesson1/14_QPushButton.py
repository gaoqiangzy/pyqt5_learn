'''
按钮控件QPushButton
QAbstractButton (父类)

QPushButton
AToolButton：工具条按钮
QRadioButton：单选按钮
QCheckbox：多选按钮

'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class QLineEditMask(QDialog):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')
        layout = QVBoxLayout()  # 使用垂直布局

        self.button1 = QPushButton("第1个按钮")
        self.button1.setText("First Button1")       # 设置按钮的文本
        self.button1.setCheckable(True)  # 是该按钮具备可选状态
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)

        # 在文本前面显示图像
        self.button2 = QPushButton("图像按钮")
        self.button2.setIcon(QIcon(QPixmap("./1.jpg")))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))

        # 设置按钮不可用
        self.button3 = QPushButton("不可用的按钮")
        self.button3.setEnabled(False)

        self.button4 = QPushButton("&MyButton")
        self.button4.setDefault(True)       # 一个布局中只允许有一个默认按钮
        self.button4.clicked.connect(lambda :self.whichButton(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)
        self.resize(400,300)

    def whichButton(self, btn):
        print("被单击的按钮是<" + btn.text() + ">")

    def buttonState(self):
        if self.button1.isChecked():
            print("按钮1已经被选中")
        else:
            print("按钮1未被选中")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()
    sys.exit(app.exec_())
