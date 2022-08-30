'''
下拉列表控件（QSpinBox）
    1、如何将列表项添加到QComBox控件中
    2、如何获取选中的列表项
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计数器控件演示')
        self.resize(300, 100)
        self.setWindowIcon(QIcon('./images/doc.ico'))

        layout = QVBoxLayout()  # 使用水平布局

        self.label=QLabel("当前值")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.sb=QSpinBox()  # 设置计数器控件
        self.sb.setValue(18)    # 设置当前默认值
        self.sb.setRange(10,999)    # 设置当前竖直范围
        self.sb.setSingleStep(3)    # 设置每次数值变化的步长
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)


    def valueChange(self):
        self.label.setText("当前值："+str(self.sb.value()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())
