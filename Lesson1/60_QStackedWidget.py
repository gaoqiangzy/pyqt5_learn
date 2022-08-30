
# 堆栈窗口控件（QStackedWidget）

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        self.setGeometry(600, 500, 400, 150)
        self.setWindowTitle('堆栈窗口控件（QStackedWidget）')

        self.list = QListWidget()       # 创建列表控件
        self.list.insertItem(0,'联系方式')
        self.list.insertItem(1,'个人信息')
        self.list.insertItem(2,'教育程度')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.stack = QStackedWidget()       # 创建堆栈窗口控件
        self.stack.addWidget(self.stack1)       # 将创建的窗口添加至堆栈窗口控件中
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()        # 创建水平布局，左侧显示列表，右侧显示堆栈的页面
        hbox.addWidget(self.list)       #
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)       # 为列表添加一个事件，即当前行变化
    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())

        self.stack1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())

        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)

    def display(self,index):
        self.stack.setCurrentIndex(index)       # 即根据索引，切换堆栈窗口中的页面

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())

