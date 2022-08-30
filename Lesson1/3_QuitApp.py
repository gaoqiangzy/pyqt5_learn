"""
QMainWindow:主窗口
QApplication:创建应用程序
QHBoxLayout:水平布局
QWidget：控件
"""
import sys

from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle("退出应用程序")

        # 添加button
        self.button1 = QPushButton("退出应用程序")
        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        # 创建水平布局
        layout = QHBoxLayout()
        # 将组件添加到水平布局上
        layout.addWidget(self.button1)

        # 创建所有控件的根
        mainFrame = QWidget()
        # 将水平布局放在根上
        mainFrame.setLayout(layout)
        # 将主框架放在整个窗口上
        self.setCentralWidget(mainFrame)

    # 按钮点击事件
    def onClick_Button(self):
        sender = self.sender()   # 通过sender()来获取button
        print(sender.text() + " 按钮被按下")
        app = QApplication.instance()  # 得到实例，
        app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./1.jpg"))
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())