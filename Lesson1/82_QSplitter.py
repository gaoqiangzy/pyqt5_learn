# 拖动控件之间的边界（QSplitter）

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle('QSplitter 例子')
        self.setGeometry(300, 300, 300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)        # 设置成面板

        splitter1 = QSplitter(Qt.Horizontal)        # 表示水平拖动
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([200,100])           # 表示水平方向两侧的宽度占比

        splitter2 = QSplitter(Qt.Vertical)          # 表示垂直拖动
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setSizes([250,50])            # 表示垂直方向两侧的高度占比


        hbox.addWidget(splitter2)
        self.setLayout(hbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Splitter()
    demo.show()
    sys.exit(app.exec_())
