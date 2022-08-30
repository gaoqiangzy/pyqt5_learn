
# 按列排序
# 1. 按哪一列排序
# 2. 排序类型：升序或降序
# sortItems(columnIndex，orderType）      第一个参数：列索引；第二个参数：排序类型

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("按列排序")
        self.resize(430, 230);
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()       # 创建表格控件
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        newItem = QTableWidgetItem('张三')
        self.tableWidget.setItem(0,0,newItem)

        newItem=QTableWidgetItem('男')
        self.tableWidget.setItem(0,1,newItem)

        newItem=QTableWidgetItem('165')
        self.tableWidget.setItem(0,2,newItem)

        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('王五')
        self.tableWidget.setItem(2, 0, newItem)

        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(2, 1, newItem)

        newItem = QTableWidgetItem('170')
        self.tableWidget.setItem(2, 2, newItem)


        self.button = QPushButton('排序')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType = Qt.DescendingOrder     # 排序类型      默认的是降序
        self.setLayout(layout)


    def order(self):
        if self.orderType == Qt.DescendingOrder:        # 如果当前是降序排列，则调整为升序排列
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder         # 如果当前为升序排列，则调整为降序排列
        self.tableWidget.sortItems(2,self.orderType)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ColumnSort()
    example.show()
    sys.exit(app.exec_())

