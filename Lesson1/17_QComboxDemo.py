'''
下拉列表控件
    1、如何将列表项添加到QComBox控件中
    2、如何获取选中的列表项
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class QComboxDemo(QWidget):
    def __init__(self):
        super(QComboxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件演示')
        self.resize(300, 100)
        layout = QVBoxLayout()  # 使用垂直布局

        self.label = QLabel("请选择编程语言")

        self.cb = QComboBox()
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["Java", "C#", "Ruby"])  # 也可以添加列表

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()     # 自适应调整尺寸

        for count in range(self.cb.count()):
            print("item" + str(count) + "=" + self.cb.itemText(count))
        print("current index", i, "select changed", self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboxDemo()
    main.show()
    sys.exit(app.exec_())
