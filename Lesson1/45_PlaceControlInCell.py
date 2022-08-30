
# 在单元格中放置控件
# setItem：将文本放到单元格中
# setCellWidget：将控件放到单元格中
# setStyleSheet：设置控件的样式（QSS）


import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView,
                              QComboBox, QPushButton)


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(430, 300);
        layout = QHBoxLayout()
        tableWidget = QTableWidget()        # 创建QTableWidget控件
        tableWidget.setRowCount(4)          # 为QTableWidget指定行数
        tableWidget.setColumnCount(3)       # 为QTableWidget指定列数

        layout.addWidget(tableWidget)       # 将QTableWidget添加到布局中

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])     # 为QTableWidget添加水平的头
        textItem = QTableWidgetItem('小明')
        tableWidget.setItem(0,0,textItem)           # setItem：将文本放到单元格中

        combox = QComboBox()        # 创建下拉列表控件
        combox.addItem('男')
        combox.addItem('女')
        # QSS Qt StyleSheet
        combox.setStyleSheet('QComboBox{margin:3px};')      # setStyleSheet 设置空间的样式属性
        tableWidget.setCellWidget(0,1,combox)           # setCellWidget：将控件放到单元格中

        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)      # 设置空间默认的是按下的状态
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tableWidget.setCellWidget(0,2,modifyButton)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PlaceControlInCell()
    example.show()
    sys.exit(app.exec_())

