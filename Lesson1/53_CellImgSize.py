

# 改变单元格中图片的尺寸
#
# setIconSize(QSize(width,height))



import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("改变单元格中图片的尺寸")
        self.resize(1000, 900)
        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setIconSize(QSize(300,200))         # 设置表格内图像的像素值
        tablewidget.setRowCount(5)          # 设置表格的行数
        tablewidget.setColumnCount(3)       # 设置表格的列数

        tablewidget.setHorizontalHeaderLabels(['图片1', '图片2', '图片3'])

        # 让列的宽度和图片的宽度相同
        for i in range(3):
            tablewidget.setColumnWidth(i,300)       # 设置表格的列宽度

        # 让行的高度和图片的高度相同
        for i in range(15):
            tablewidget.setRowHeight(i,200)         # 设置表格的行宽度

        for k in range(1,4):
            i = k / 3   # 行
            j = k % 3   # 列
            item = QTableWidgetItem()
            item.setIcon(QIcon('C:/GaoQiang/work/codes/web/pyqt5_learn/pyqt5_learn/images/%d.png' % k))       # 改变单元格中图像的尺寸
            tablewidget.setItem(i,j,item)

        layout.addWidget(tablewidget)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellImageSize()
    example.show()
    sys.exit(app.exec_())

