#
# QTreeView控件与系统定制模式
#
# QTreeWidget
#
# Model

# QDirModel       # 用来显示当前操作系统的目录结构


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = QDirModel()     # 用于显示目录结构的模型
    tree = QTreeView()      # chuangjkia
    tree.setModel(model)

    tree.setWindowTitle("QTreeView")
    tree.resize(600,400)
    tree.show()


    sys.exit(app.exec_())

