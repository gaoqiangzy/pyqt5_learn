'''

绘制不同类型的直线

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)


        pen = QPen(Qt.red,3,Qt.SolidLine)       # 创建画笔（颜色、画笔粗细、线型）

        painter.setPen(pen)             # 设置对象
        painter.drawLine(20,40,250,40)          # 设置其实位置

        pen.setStyle(Qt.DashLine)       # 设置不同的线类型-------设置完线的风格后，必须得重新设置下pen对象，否则不会起作用
        painter.setPen(pen)             # 必须得重新设置下pen对象，否则不会起作用
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)             # 必须得重新设置下pen对象，否则不会起作用
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)     # Qt.CustomDashLine：设置自定义的线
        pen.setDashPattern([1,10,5,8])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)


        painter.end()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())

