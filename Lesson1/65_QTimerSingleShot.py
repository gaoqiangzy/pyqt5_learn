
# 让程序定时关闭
# QTimer.singleShot


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=140><b>Hello World，窗口在5秒后自动关闭!</b></font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)          # 设置窗口的标题栏隐藏，并且是无框架窗口
    label.show()
    QTimer.singleShot(10000,app.quit)        # 即在一段时间后执行代码一次

    sys.exit(app.exec_())

