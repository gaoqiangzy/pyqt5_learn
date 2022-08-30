
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QHBoxLayout,QWidget,QToolTip,QPushButton       # QMainWindow:主窗口;QApplication:创建应用程序 ;QDesktopWidget:用于获取桌面信息参数
from PyQt5.QtGui import QIcon           # 用来添加图标
from PyQt5.QtGui import QFont

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()
        self.initUI()

    def initUI(self):
        # 设置字体
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip("今天是<b>星期五</b>")
        self.setGeometry(300,200,200,300)
        self.resize(250,250)
        # 设置主窗口的标题
        self.setWindowTitle("设置控件提示信息")
        # 设置窗口图标
        self.setWindowIcon(QIcon("./images/Dragon.ico"))        # 设置窗口图标方式

        self.button1 = QPushButton("我的按钮")
        self.button1.setToolTip("这是一个按钮，Are you ok?")

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/Dragon.ico"))     # 设置应用程序的图标
    main_ = CenterForm()
    main_.show()
    sys.exit(app.exec())
