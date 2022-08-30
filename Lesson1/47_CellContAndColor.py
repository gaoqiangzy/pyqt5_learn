
# 设置单元格字体和颜色



import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtGui import QBrush, QColor, QFont


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")
        self.resize(430, 230);
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times',14,QFont.Black))
        newItem.setForeground(QBrush(QColor(255,0,0)))      # setForeground：设置字体的颜色，借助QBrush
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('女生')
        newItem.setForeground(QBrush(QColor(255,255,0)))
        newItem.setFont(QFont('Times', 20))     # 设置文字的字体与字号
        newItem.setBackground(QBrush(QColor(0,0,255)))       # setBackground：设置背景色
        tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times',20,QFont.Black))      # 设置文字的字体与字号、颜色
        newItem.setForeground(QBrush(QColor(0,0,255)))      # setForeground：设置字体的颜色，借助QBrush
        tableWidget.setItem(0,2,newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellFontAndColor()
    example.show()
    sys.exit(app.exec_())
