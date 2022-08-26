import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Ico(QWidget):

   def __init__(self):
       super().__init__()
       self.initUI()

   def initUI(self):
        # 定位窗口，并设置窗口大小（x,y,w,h）  = resize()+move()方法的结合
       self.setGeometry(300, 300, 300, 220)
       self.setWindowTitle('自定义标日')
       self.setWindowIcon(QIcon('xdbcb8.ico'))

       self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())