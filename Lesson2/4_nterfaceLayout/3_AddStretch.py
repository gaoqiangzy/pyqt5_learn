import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')

        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1) #增加伸缩量
        hbox.addWidget(bt1)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(bt2)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(bt3)
        hbox.addStretch(6)#增加伸缩量
        """
        四个addStretch()函数用于在button按钮间增加伸缩量，伸缩量的比例为1:1:1:6，
        意思就是将button以外的空白地方按设定的比例等分为9份并按照设定的顺序放入布局器中。
        """
        self.setLayout(hbox)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())