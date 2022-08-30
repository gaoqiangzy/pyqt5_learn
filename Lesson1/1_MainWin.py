import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()

        # 设置标题
        self.setWindowTitle("第一个主窗口应用")

        # 设置窗口尺寸
        self.resize(400,300)

        # 状态栏
        self.status = self.statusBar()

        # 在状态栏上显示信息
        self.status.showMessage("只存在5秒的信息",5000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./1.jpg'))
    main_ = FirstMainWin()
    main_.show()
    sys.exit((app.exec()))