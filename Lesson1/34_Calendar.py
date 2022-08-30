'''
日历控件
QCalendarWidget
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()
    def initUI(self):
        self.cal = QCalendarWidget(self)    # 创建日历控件
        self.cal.setMinimumDate(QDate(1988,1,1))        # 设置允许显示的最小日期
        self.cal.setMaximumDate(QDate(2088,1,1))        # 设置允许显示的最大日期

        self.cal.setGridVisible(True)       # 设置日期以网格的形式显示

        self.cal.move(20,20)
        self.cal.clicked.connect(self.showDate)
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20,300)

        self.resize(400,350)
        self.setWindowTitle("日历演示")

    def showDate(self,date):
        #self.label.setText((date.toString("yyyy-MM-dd dddd")))
        self.label.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())

