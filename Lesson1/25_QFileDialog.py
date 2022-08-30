'''
文件对话框：QFileDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()      # 创建垂直布局
        self.button1 = QPushButton('加载图片')      # 创建点击控件
        self.button1.clicked.connect(self.loadImage)        # 绑定点击事件
        layout.addWidget(self.button1)                      # 将按钮添加到垂直布局

        self.imageLabel = QLabel()          # 创建Label，并将图像显示在上面
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents = QTextEdit()         # 创建多行文本控件
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle('文件对话框演示 ')

    def loadImage(self):
        fname,_ = QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)     # 设置打开文件的模式---即打开任何文件
        dialog.setFilter(QDir.Files)        # 选择文件

        if dialog.exec():       # 打开文件
            filenames = dialog.selectedFiles()
            f = open(filenames[0],encoding='utf-8',mode='r')
            with f:
                data = f.read()
                self.contents.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
