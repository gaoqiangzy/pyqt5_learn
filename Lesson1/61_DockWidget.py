
# 停靠控件（QDockWidget）

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)

        self.setWindowTitle("停靠控件（QDockWidget）")

        self.items = QDockWidget('Dockable',self)         # 创建停靠控件
        self.listWidget = QListWidget()                   # 创建列表控件
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        self.items.setWidget(self.listWidget)       # 将列表控件添加至停靠控件中

        self.setCentralWidget(QLineEdit())      # 在当前窗口放置一个QLineEdit控件

        # self.items.setFloating(True)        # 设置停靠窗口默认是悬浮的状态
        self.items.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea,self.items)           # 在当前窗口中添加停留控件，并设置默认停靠的区域




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())

