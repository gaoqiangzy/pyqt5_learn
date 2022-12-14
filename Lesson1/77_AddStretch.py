
# 设置伸缩量（addStretch）

import sys,math
from PyQt5.QtWidgets import *

class Stretch(QWidget) :
    def __init__(self):
        super(Stretch,self).__init__()
        self.setWindowTitle("设置伸缩量")
        self.resize(800,100)
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn4 = QPushButton(self)
        btn5 = QPushButton(self)
        btn1.setText("按钮1")
        btn2.setText("按钮2")
        btn3.setText("按钮3")
        btn4.setText("按钮4")
        btn5.setText("按钮5")

        layout = QHBoxLayout()      # 创建水平盒子布局

        layout.addStretch(0)        # 设置拉伸比例        伸缩量设置为0，表示先把控件给排列了，剩下的不是0的伸缩量再用剩余的空间排列
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        btnOK = QPushButton(self)
        btnOK.setText("确定")
        btnCancel = QPushButton(self)
        btnCancel.setText("取消")
        layout.addStretch(1)        # 表示的是距离的倍数         重设拉伸比例

        layout.addWidget(btnOK)
        layout.addWidget(btnCancel)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Stretch()
    main.show()
    sys.exit(app.exec_())

