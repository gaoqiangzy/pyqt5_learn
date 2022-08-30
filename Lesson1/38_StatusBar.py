
# 创建和使用状态栏


import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow) :
    def __init__(self):
        super(StatusBar,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("状态栏演示")
        self.resize(300,200)

        bar = self.menuBar()        # 创建顶层菜单
        file = bar.addMenu("File")      # 创建子菜单
        file.addAction("show")
        file.triggered.connect(self.processTrigger)     # 绑定菜单触发动作
        self.setCentralWidget(QTextEdit())      # 在窗口放置中心的控件

        self.statusBar = QStatusBar()       # 创建状态栏对象
        self.setStatusBar(self.statusBar)       # 设置状态栏


    def processTrigger(self,q):
        if q.text() == "show" :
            self.statusBar.showMessage(q.text() + " 菜单被点击了",5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec_())
