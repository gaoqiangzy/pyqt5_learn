import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()

        self.setWindowTitle("设置窗口在桌面的位置")

        self.resize(400,300)

    def center(self):
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕坐标
        size = self.geometry()  # 获取窗口的坐标系

        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2

        self.move(newLeft,newTop)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./1.jpg'))
    main_ = CenterForm()
    main_.show()
    sys.exit(app.exec())