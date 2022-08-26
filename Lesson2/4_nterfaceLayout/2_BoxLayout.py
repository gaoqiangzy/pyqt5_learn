import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout)


"""
窗口的右下角放置了三个按钮。 当我们调整应用程序窗口大小时，它们会留在那里，我们同时使用一个HBoxLayout和一个QVBoxLayout。
"""
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
        """
        addStretch函数的作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零，
        会将你放在layout中的空间压缩成默认的大小。例如用addStretch函数实现将QHBoxLayout的布局器的空白空间分配。
        """
        # 建一个水平框布局，并添加一个拉伸因子和三个按钮。这个拉伸在三个按钮之前增加了一个可伸缩的空间。这将把它们推到窗口的右边。
        hbox.addStretch(1)  # 拉伸因子
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)

        # 水平布局放置在垂直布局中。垂直框中的拉伸因子将按钮的水平框推到窗口的底部。
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())