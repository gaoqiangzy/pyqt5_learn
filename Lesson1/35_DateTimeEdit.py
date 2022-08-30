'''
输入各种风格的日期和时间

QDateTimeEdit

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DateTimeEdit(QWidget):
    def __init__(self):
        super(DateTimeEdit, self).__init__()
        self.initUI()
    def initUI(self):
        vlayout = QVBoxLayout()

        dateTimeEdit1 = QDateTimeEdit()     # 创建时间控件
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))     # 设置最小日期   减去365天
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))      # 设置最大日期  加上365天
        self.dateTimeEdit = dateTimeEdit1
        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())  # 创建时间控件并传入当前时间
        dateTimeEdit2.setCalendarPopup(True)    # 为True：表示可以通过日历控件设置
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")


        dateEdit = QDateTimeEdit(QDate.currentDate())
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit = QDateTimeEdit(QTime.currentTime())
        timeEdit.setDisplayFormat("HH:mm:ss")

        # 第一个控件变化触发事件
        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)

        self.btn = QPushButton('获取日期和时间')
        self.btn.clicked.connect(self.onButtonClick)
        vlayout.addWidget(self.btn)
        self.setLayout(vlayout)

        self.resize(300,90)
        self.setWindowTitle("设置不同风格的日期和时间")

    # 日期变化
    def onDateChanged(self,date):
        print(date)

    # 时间变化
    def onTimeChanged(self,time):
        print(time)

    # 日期和时间变化
    def onDateTimeChanged(self,datetime):
        print(datetime)

    def onButtonClick(self):
        datetime = self.dateTimeEdit.dateTime()
        print(datetime)

        # 最大日期
        print(self.dateTimeEdit.maximumDate())
        # 最大日期和时间
        print(self.dateTimeEdit.maximumDateTime())

        # 最小日期
        print(self.dateTimeEdit.minimumDateTime())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeEdit()
    main.show()
    sys.exit(app.exec_())
