
# 设置单元格尺寸
# setRowHeight()     # 设置单元格行的高度
# setColumnWidth()      # 设置单元格列的宽度

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QColor, QFont

class CellSize(QWidget):
    def __init__(self):
        super(CellSize,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(530, 300);
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.resize(250, 250)
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        tableWidget.setRowHeight(0, 80)     # 设置单元格的尺寸----（0,80）即表示改变第一行的高度为80
        tableWidget.setColumnWidth(2, 120)      # 设置单元格的尺寸------（2,120）即表示改变第三列的宽度为120
        tableWidget.setRowHeight(2,100)
        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times',10,QFont.Black))
        newItem.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('女')
        newItem.setForeground(QBrush(QColor(255,255,0)))
        newItem.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times',10,QFont.Black))
        newItem.setForeground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,2,newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellSize()
    example.show()
    sys.exit(app.exec_())

