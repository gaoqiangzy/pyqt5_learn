#!/usr/bin/python3

# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')  # 提示
        self.bt1.clicked.connect(self.showMessage)

        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()  # 将'在这里输入数字'全选， 方便输入数字，否则还得手动全选删除默认字符
        self.text.setFocus()  # 让焦点置于文本栏中，不然还得手动在文本栏中单击一下
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):

        guessnumber = int(self.text.text())
        print(self.num)

        if guessnumber > self.num:
            # QMessageBox.about就是弹出一个对话框，告诉你结果是什么样的，此外还有question、critical、warning、information
            # QMessageBox对话框包含类型只是图标不同其他无太大差别
            QMessageBox.about(self, '看结果', '猜大了!')
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    # 如果关闭QWidget，则生成QCloseEvent。 要修改widget的行为，我们需要重新实现closeEvent（）事件处理程序。
    def closeEvent(self, event):
        # 第一个字符串出现在标题栏上。 第二个字符串是对话框显示的消息文本。 第三个参数指定出现在对话框中的按钮的组合。 最后一个参数是默认按钮。
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  # exec_（） 应用程序进入主循环。 主循环获取事件并将其发送到对象。