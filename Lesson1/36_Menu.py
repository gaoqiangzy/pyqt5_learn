'''
创建和使用菜单
'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Menu(QMainWindow) :
    def __init__(self):
        super(Menu,self).__init__()
        self.resize(300,300)
        bar = self.menuBar()  # 获取菜单栏

        file = bar.addMenu("文件")
        file.addAction("新建")        # 利用文本创建        （方式一）

        save = QAction("保存",self)                   #（方式二）
        save.setShortcut("Ctrl + S")    # 设置快捷键
        file.addAction(save)        # 也可以利用带有动作的菜单创建
        save.triggered.connect(self.process)

        quit = QAction("退出", self)
        file.addAction(quit)


        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")


    def process(self,a):
        print(self.sender().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())
