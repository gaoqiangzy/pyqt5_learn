import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

# 获取鼠标的坐标，及绘制一条线，线的起点坐标为(0,0)
class Example(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)  # 启用鼠标跟踪
    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('学点编程吧')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)  # 勾股定理计算鼠标到中心点距离
        self.label.setText('坐标: ( x: %d ,y: %d )' % (event.x(), event.y()) + " 离中心点距离: " + str(distance_from_center))
        self.pos = event.pos()
        self.update()  # 更新图形

    # 重写绘图事件
    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())