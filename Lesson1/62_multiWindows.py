
# 容纳多文档的窗口
# QMdiArea
# QMdiSubWindow


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MultiWindows(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MultiWindows, self).__init__(parent)

        self.setWindowTitle("容纳多文档的窗口")

        self.mdi = QMdiArea()       # 创建可以容纳多个子窗口的窗口（相当于窗口的容器）
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()        # 创建菜单栏对象
        file = bar.addMenu("File")  # 添加菜单
        file.addAction("New")       # 添加子菜单
        file.addAction("cascade")   # 添加子菜单
        file.addAction("Tiled")     # 添加子菜单

        file.triggered.connect(self.windowaction)       # 给菜单添加点击动作
    def windowaction(self,q):
        print(q.text())
        if q.text() == "New":
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()       # 创建子窗口
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)      # 将子窗口添加到窗口容器
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()    # 设置层叠方式
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()       # 设置层叠方式



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MultiWindows()
    demo.show()
    sys.exit(app.exec_())

