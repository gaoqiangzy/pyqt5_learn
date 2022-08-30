'''
用画刷填充图形区域
'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class FillRect(QWidget):
    def __init__(self):
        super(FillRect,self).__init__()
        self.resize(600,600)
        self.setWindowTitle('用画刷填充区域')

    def paintEvent(self,e):
        qp = QPainter()     # 获得一个画布
        qp.begin(self)
        brush = QBrush(Qt.SolidPattern)     # 创建画刷对象，，Qt.SolidPattern：实型模式
        qp.setBrush(brush)      # 设置画刷对象
        qp.drawRect(10,15,90,60)        # 绘制矩形

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130,15,90,60)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250,15,90,60)

        brush = QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FillRect()
    main.show()
    sys.exit(app.exec_())
