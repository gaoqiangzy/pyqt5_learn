# 选项卡控件：QTabWidget

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TabWidgetDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidgetDemo, self).__init__(parent)

        self.setWindowTitle("选项卡控件：QTabWidget")

        # 创建用于显示控件的窗口
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.resize(300,00)
        # 将三个窗口与三个选项卡绑定
        self.addTab(self.tab1,'选项卡1')       # 第一个参数是窗口对象，第二个参数是选项卡的名称
        self.addTab(self.tab2,'选项卡2')
        self.addTab(self.tab3,'选项卡3')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QFormLayout()      # 创建表单控件
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())
        self.setTabText(0,'联系方式')       # 设置选项卡的标题
        self.tab1.setLayout(layout)     # 将表单控件进行装载

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()

        sex_QRadio=QRadioButton('男')
        sex_QRadio.setChecked(True)     # 设置复选框默认选中状态
        sex.addWidget(sex_QRadio)
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())
        self.setTabText(1,'个人详细信息')     # 设置选项卡的标题
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.setTabText(2,'教育程度')
        self.tab3.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabWidgetDemo()
    demo.show()
    sys.exit(app.exec_())

