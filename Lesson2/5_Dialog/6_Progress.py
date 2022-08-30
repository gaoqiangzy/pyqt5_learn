# coding=utf-8

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog)
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle("进度对话框")

        self.lb = QLabel("文件数量", self)
        self.lb.move(20, 40)

        self.bt1 = QPushButton('开始', self)
        self.bt1.move(20, 80)

        self.edit = QLineEdit('100000', self)
        self.edit.move(100, 40)

        self.show()

        self.bt1.clicked.connect(self.showDialog)

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)   # 对话框出现之前必须通过的时间。 5s,如果任务的预期持续时间小于minimumDuration，则对话框根本不会出现。
        progress.setWindowModality(Qt.WindowModal)  # 保留由模态小部件阻止的窗口。
        progress.setRange(0, num)
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():  # 判断是否按下取消按钮
                QMessageBox.warning(self, "提示", "操作失败")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())