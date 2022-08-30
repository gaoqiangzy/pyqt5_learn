"""
QLabel与伙伴控件
mainlayout.addWidget(控件对象,行索引,列索引,占用多少行,占用多少列)

"""

from PyQt5.QtWidgets import *
import sys


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件")
        nameLabel = QLabel("&Name", self)  # 同时设置热键
        nameLineRdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineRdit)

        passwordLabel = QLabel("&PassWord", self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton("&OK")  # 创建按钮
        btnCancel = QPushButton("&Cancel")

        # 使用栅格布局
        mainlayout = QGridLayout(self)
        mainlayout.addWidget(nameLabel, 0, 0)
        mainlayout.addWidget(nameLineRdit, 0, 1, 1, 2)  # 表示放置在第0行，第1列，占用一行两列

        mainlayout.addWidget(passwordLabel, 1, 0)
        mainlayout.addWidget(passwordLineEdit, 1, 1, 1, 2)  # 表示放置在第1行，第1列，占用一行两列

        mainlayout.addWidget(btnOK, 2, 1)
        mainlayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/Dragon.ico"))     # 设置应用程序的图标
    main_ = QLabelBuddy()
    main_.show()
    sys.exit(app.exec())
