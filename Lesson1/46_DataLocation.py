
# 在表格中快速定位到特定的行
# 1. 数据的定位：findItems  返回一个列表
# 2. 如果找到了满足条件的单元格，会定位到单元格所在的行：setSliderPosition(row)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush
class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(600, 800);

        layout = QHBoxLayout()
        tableWidget = QTableWidget()        # 创建QTableWidget对象
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)

        layout.addWidget(tableWidget)

        for i in range(40):     # 对行循环
            for j in range(4):      # 对列循环
                itemContent = '(%d,%d)' %(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(itemContent))
        self.setLayout(layout)


        """*********开始搜索满足条件的Cell*********"""
        # 搜索满足条件的Cell
        text = '(1'     # 表示要搜索的文本内容
        items = tableWidget.findItems(text,QtCore.Qt.MatchStartsWith)       # QtCore.Qt.MatchStartsWith：表示搜索的模式  （模糊匹配）
                                                                            # QtCore.Qt.MatchExactly：表示精确匹配

        if len(items) > 0:
            item = items[0]     # 即满足条件的第一个值
            item.setBackground(QBrush(QColor(0,255,0)))     # 设置背景色
            item.setForeground(QBrush(QColor(255,0,0)))     # 设置文字的颜色

            row = item.row()        # 获取当前项所在的行

            # 定位到指定的行
            tableWidget.verticalScrollBar().setSliderPosition(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DataLocation()
    example.show()
    sys.exit(app.exec_())
