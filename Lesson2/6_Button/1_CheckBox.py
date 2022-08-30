"""
QCheckBox（复选框）和QRadioButton（单选框）都是选项按钮。这是因为它们都可以在开（选中）或者关（未选中）之间切换。区别是对用户选择的限制：单选框定义了“多选一”的选择，而复选框提供的是“多选多”的选择。
只要复选框被选中或者清除，都会发射一个stateChanged()信号。如果想在复选框状态改变的时候触发一个行为，请连接这个信号，可以使用 isChecked()来查询复选框是否被选中。
除了常用的选中和未选中两个状态，QCheckBox还可选地提供了第三种状态（半选）。如果需要第三种状态，可以通过setTristate()来使它生效，并使用checkState()来查询当前的切换状态。
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.cb1 = QCheckBox('全选', self)
        self.cb2 = QCheckBox('你是', self)
        self.cb3 = QCheckBox('我的', self)
        self.cb4 = QCheckBox('宝贝', self)

        bt = QPushButton('提交', self)

        # 为减少行数，部分非重要代码省略....
        self.resize(300, 200)
        self.setWindowTitle('关注微信公众号：学点编程吧--复选框')

        self.cb1.move(20, 20)
        self.cb2.move(30, 50)
        self.cb3.move(30, 80)
        self.cb4.move(30, 110)

        bt.move(20, 160)

        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        bt.clicked.connect(self.go)

        self.show()

    def go(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的宝贝！')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的！')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是宝贝！')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '我的宝贝！')
        elif self.cb2.isChecked():
            QMessageBox.information(self, 'I Love U', '你是！')
        elif self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '我的！')
        elif self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '宝贝！')
        else:
            QMessageBox.information(self, 'I Love U', '貌似你没有勾选啊！')

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)

    def changecb2(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setCheckState(Qt.Checked)
        elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
            self.cb1.setTristate()
            self.cb1.setCheckState(Qt.PartiallyChecked)  # 半选
        else:
            self.cb1.setTristate(False)
            self.cb1.setCheckState(Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())