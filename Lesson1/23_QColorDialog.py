'''
颜色对话框：（QColorDialog）
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog例子')
        layout = QVBoxLayout()
        self.colorButton = QPushButton('设置颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton1 = QPushButton('设置背景颜色')
        self.colorButton1.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel = QLabel('Hello，测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)  # 将布局放入窗口

    def getColor(self):
        color = QColorDialog.getColor()  # 获取颜色
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(p)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()  # 调色板控件
        p.setColor(QPalette.Window, color)  # 设置颜色
        # self.colorLabel.setAutoFillBackground(True)         # 设置背景色自动填充
        # self.colorLabel.setPalette(p)

        self.setAutoFillBackground(True)  # 设置背景色自动填充
        self.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())
