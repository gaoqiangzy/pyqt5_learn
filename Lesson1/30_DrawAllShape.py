"""
绘制各种图形

弧
圆形
椭圆
矩形（正方形）
多边形
绘制图像

"""

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll,self).__init__()
        self.resize(300,600)
        self.setWindowTitle('绘制各种图形')
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(Qt.blue)      # 设置笔的颜色
        # 绘制弧
        rect = QRect(0,10,100,100)  # 绘制弧，需要先确定矩形区域    前两个参数为顶点坐标，后两个参数为宽度与高度
        # alen: 1个alen等于1/16度   45 * 16
        qp.drawArc(rect,0, 50 * 16)     #       drawArc（弧形区域，起始的角度，结束的角度）


        # 通过弧绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120,10,100,100,0, 360 * 16)

        # 绘制带弦的弧
        qp.drawChord(10,120,100,100,12,130*16)

        # 绘制扇形
        qp.drawPie(10,240,100,100,12,130*16)

        # 椭圆
        qp.drawEllipse(120,120,150,100)


        # 绘制5边形
        point1 = QPoint(140,380)
        point2 = QPoint(270,420)
        point3 = QPoint(290,512)
        point4 = QPoint(290,588)
        point5 = QPoint(200,533)
        polygon = QPolygon([point1,point2,point3,point4,point5])        # 绘制多边形对象
        # 绘制多边形图像
        qp.drawPolygon(polygon)


        # 将一个图像绘制到窗口上
        image = QImage('./1.jpg')        # 装载图像
        rect = QRect(10, 400, image.width()/3, image.height()/3)        # 指定将图像绘制到多大的区域
        #image.save('./images/book1.png')
        qp.drawImage(rect,image)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())
