
import sys
"""
    窗口的setWindowIcon方法用于设置窗口的图标，只在Windows中可用
    QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序图标，但调用了窗口的setWindowIcon方法
    QApplication中的setWindowIcon方法就只能设置应用程序图标了

"""
# QDesktopWidget        通过此API得到整个屏幕的尺寸

from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget        # QMainWindow:主窗口;QApplication:创建应用程序 ;QDesktopWidget:用于获取桌面信息参数
from PyQt5.QtGui import QIcon           # 用来添加图标

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,250)
        # 设置主窗口的标题
        self.setWindowTitle("设置窗口图标")
        # 设置窗口图标
        self.setWindowIcon(QIcon("./1.jpg"))        # 设置窗口图标方式


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/Dragon.ico"))     # 设置应用程序的图标
    main_ = CenterForm()
    main_.show()
    sys.exit(app.exec())
