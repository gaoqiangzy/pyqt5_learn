
# 使用打印机

from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *
import sys

class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport,self).__init__()
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton('打印QTextEdit控件中的内容',self)
        self.button.setGeometry(20,20,260,30)   # 设置按钮控件的位置
        self.button.clicked.connect(self.print)

        self.editor = QTextEdit('默认文本',self)
        self.editor.setGeometry(20,60,260,200)



    def print(self):
        printer = QtPrintSupport.QPrinter()     # 创建打印对象

        painter = QtGui.QPainter()      # 获得一个画布
        # 将绘制的目标重定向到打印机
        painter.begin(printer)      # 将数据绘制到打印机
        screen = self.editor.grab()     # 获取控件内所有的内容
        painter.drawPixmap(10,10,screen)        # 把内容当成一个图来打印           ----（10，,10表示从该坐标处开始打印，而非定格打印）
        painter.end()
        print("print")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PrintSupport()
    gui.show()
    app.exec_()

