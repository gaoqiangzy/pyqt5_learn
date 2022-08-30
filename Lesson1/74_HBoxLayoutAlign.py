
# 设置控件的对齐方式


import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class HBoxLayoutAlign(QWidget) :
    def __init__(self):
        super(HBoxLayoutAlign,self).__init__()
        self.setWindowTitle("水平盒布局")

        hlayout = QHBoxLayout()     # 水平盒布局
        hlayout.addWidget(QPushButton('按钮1'),2,Qt.AlignLeft | Qt.AlignTop)          # 第一个参数是：传入的控件；第二个参数是：拉伸所占的控件的比例；第三个参数是：对齐方式
        hlayout.addWidget(QPushButton('按钮2'),4,Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('按钮3'),1,Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('按钮4'),1,Qt.AlignLeft | Qt.AlignBottom)
        hlayout.addWidget(QPushButton('按钮5'),1,Qt.AlignLeft | Qt.AlignBottom)
        hlayout.setSpacing(40)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayoutAlign()
    main.show()
    sys.exit(app.exec_())

