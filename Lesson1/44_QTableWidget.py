
# 扩展的表格控件（QTableWidget）
# QTableWidget是QTableView的子类
# 每一个Cell（单元格）是一个QTableWidgetItem



import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView)


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget演示")
        self.resize(430, 230);
        layout = QHBoxLayout()
        tablewidget = QTableWidget()        # 创建QTableWidget对象
        tablewidget.setRowCount(4)          # 设置行数
        tablewidget.setColumnCount(3)       # 设置列数

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])     # 设置字段名称
        nameItem = QTableWidgetItem("小明")
        tablewidget.setItem(0,0,nameItem)

        ageItem = QTableWidgetItem("24")
        tablewidget.setItem(0,1,ageItem)

        jgItem = QTableWidgetItem("北京")
        tablewidget.setItem(0,2,jgItem)

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)       # 设置禁止编辑

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 调整列和行（即行与列的大小根据内容调整）
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()

        # 隐藏或显示水平与垂直表格字段名称
        tablewidget.horizontalHeader().setVisible(True)        # 设置水平表头是否可见
        tablewidget.verticalHeader().setVisible(False)         # 设置垂直头是否课件

        tablewidget.setVerticalHeaderLabels(["a","b"])      # 设置垂直的头名称

        # 隐藏表格线
        tablewidget.setShowGrid(True)       # 设置单元格的网格线是否可见

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetDemo()
    example.show()
    sys.exit(app.exec_())
