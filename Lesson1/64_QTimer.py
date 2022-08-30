
# 动态显示当前时间
# QTimer      # 定时器类
# QThread
#
# 多线程：用于同时完成多个任务


from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
import sys

class ShowTime(QWidget):
    def __init__(self, parent=None):
        super(ShowTime, self).__init__(parent)
        self.setWindowTitle("动态显示当前时间")
        self.resize(300,150)
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        layout= QGridLayout()

        self.timer = QTimer()       # 创建定时器QTimer()对象
        self.timer.timeout.connect(self.showTime)       # 绑定时间响应函数

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()      # 获取当前时间

        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)      # 开始计时器，并设置时间间隔
        self.startBtn.setEnabled(False)     # 并且开始之后，就把该按钮设置为False
        self.endBtn.setEnabled(True)        #

    def endTimer(self):
        self.timer.stop()           # 停止计时
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ShowTime()
    form.show()
    sys.exit(app.exec_())

