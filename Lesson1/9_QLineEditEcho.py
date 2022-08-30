"""
QLineEdit控件与回显模式：
基本功能：输入单行的文本
EchoMode（设置回显模式）：
        其支持四种回显模式
        1、Normal
        2、NoEcho（不回显模式）
        3、Password：
        4、PasswordEchoOnEdit:
"""

from PyQt5.QtWidgets import *

import sys


class QLineEditEchoMode(QDialog):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框的回显模式")

        formlayout = QFormLayout()      # 创建表单布局

        # 创建控件
        normalLineEdit = QLineEdit()
        noEchoLineEdit=QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnLineEdit = QLineEdit()

        # 将控件添加到布局中
        formlayout.addRow("Normal",normalLineEdit)
        formlayout.addRow("NoEcho", noEchoLineEdit)
        formlayout.addRow("Password", passwordLineEdit)
        formlayout.addRow("passwordEchoOnLineEdit", passwordEchoOnLineEdit)

        # 为文本输入框设置placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnLineEdit.setPlaceholderText("passwordEchoOnLineEdit")

        # 设置回显模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/Dragon.ico"))     # 设置应用程序的图标
    main_ = QLineEditEchoMode()
    main_.show()
    sys.exit(app.exec())
