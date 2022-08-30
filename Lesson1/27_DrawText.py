'''

绘图API：绘制文本

1. 文本
2. 各种图形（直线，点，椭圆，弧，扇形，多边形等）
3. 图像

QPainter

painter = QPainter()

painter.begin()

painter.drawText(...)

painter.end()
必须在paintEvent事件方法中绘制各种元素

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300, 200)
        self.text = "Python从菜鸟到高手"

    # 此事件，窗口创建时会自动调用
    def paintEvent(self, event):
        painter = QPainter(self)  # 创建QPainter对象
        painter.begin(self)     # 初始化画板
        print("窗口改变")
        painter.setPen(QColor(150, 43, 5))  # 设置笔的颜色
        painter.setFont(QFont('SimSun', 25))  # 设置字体
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)  # 第一个参数表示绘制的位置
        painter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())
