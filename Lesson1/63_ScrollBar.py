
# 滚动条控件（QScrollBar）
# QScrollBar的作用
# 1. 通过滚动条值的变化控制其他控件状态的变化
# 2. 通过滚动条值的变化控制控件位置的变化

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScrollBar(QWidget):
    def __init__(self):
        super(ScrollBar, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        self.label = QLabel('拖动滚动条去改变文字颜色')

        hbox.addWidget(self.label)

        self.scrollbar1 = QScrollBar()  # 创建滚动条控件
        self.scrollbar1.setMaximum(255)  # 设置滚动条控件的最大值
        self.scrollbar1.sliderMoved.connect(self.sliderMoved)  # 绑定滚动条滑动事件

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMoved)  # 绑定滚动条滑动事件

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMoved)  # 绑定滚动条滑动事件

        self.scrollbar4 = QScrollBar()
        self.scrollbar4.setMaximum(255)
        self.scrollbar4.sliderMoved.connect(self.sliderMoved1)  # 绑定滚动条滑动事件

        hbox.addWidget(self.scrollbar1)
        hbox.addWidget(self.scrollbar2)
        hbox.addWidget(self.scrollbar3)
        hbox.addWidget(self.scrollbar4)
        self.setGeometry(300, 300, 300, 200)

        self.setLayout(hbox)  # 将水平布局添加到窗口中

        self.y = self.label.pos().y()  # 获取到QLabel控件的位置坐标

    def sliderMoved(self):
        print(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value())
        palette = QPalette()  # 创建调色板对象，用于设置颜色
        c = QColor(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)  # 给QLabel控件设置颜色

    def sliderMoved1(self):
        self.label.move(self.label.x(), self.y + self.scrollbar4.value())  # QLabel控件位置的位移动作


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ScrollBar()
    demo.show()
    sys.exit(app.exec_())

