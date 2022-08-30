"""
限制QLineEdit控件的输入（校验器）
    即限制只能输入整数、浮点数或者满足一定条件的字符串

"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator     # QIntValidator：校验整数;QDoubleValidator：校验浮点数；QRegExpValidator：检验正则表达式
from PyQt5.QtCore import QRegExp      # 正则表达式的类
import sys


class QLineEditValidator(QDialog):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("校验器")

        formlayout = QFormLayout()      # 创建表单布局

        # 创建三个控件
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        # 将三个控件添加到表单布局中
        formlayout.addRow("整数类型",intLineEdit)
        formlayout.addRow("浮点类型", doubleLineEdit)
        formlayout.addRow("数字和字母类型", validatorLineEdit)

        # 设置placeholderText
        intLineEdit.setPlaceholderText("整形")
        doubleLineEdit.setPlaceholderText("浮点型")
        validatorLineEdit.setPlaceholderText("数字和字母类型")

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)     # 设定整数范围在[1,99]

        # 浮点校验器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360,360)      # 设定浮点数范围[-360,360]
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)      # 设置正常的表示浮点数
        doubleValidator.setDecimals(2)      # 设置精度，小数点后2位

        # 字符和数字
        reg = QRegExp("[a-z0-9]+$")     # 正则表达式类
        validator = QRegExpValidator(self)      # 正则表达式校验器
        validator.setRegExp(reg)                # 将正则表达式与正则表达式校验器绑定

        # 设置校验器（即将校验器与对应的控件绑定）
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)


        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/Dragon.ico"))     # 设置应用程序的图标
    main_ = QLineEditValidator()
    main_.show()
    sys.exit(app.exec())
