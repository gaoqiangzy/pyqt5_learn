'''
让控件支持拖拽动作
A.setDragEnabled(True)      # 使的A可以被拖拽

B.setAcceptDrops(True)      # 使的B可以接受拖拽的内容

B需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发


'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox) :       # 继承QComboBox控件
    def __init__(self):
        super(MyComboBox,self).__init__()
        self.setAcceptDrops(True)       # 表示其可以接受别的控件了
    def dragEnterEvent(self,e):     # 表示别的控件拖进来后，还没有松开鼠标时触发
        print(e)
        if e.mimeData().hasText():      # 表示有文本，就接受；没有文本，就忽略
            e.accept()
        else:
            e.ignore()
    def dropEvent(self,e):      # 放下控件时触发
        self.addItem(e.mimeData().text())       # 将A控件中的文本放置到B控件内

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo,self).__init__()
        formLayout = QFormLayout()
        # formLayout.addRow("说明",QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        formLayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))

        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让QLineEdit控件可被拖动

        combo = MyComboBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())

