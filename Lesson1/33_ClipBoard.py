'''
使用剪贴板
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard,self).__init__()
        textCopyButton = QPushButton('复制文本')
        textPasteButton = QPushButton('粘贴文本')

        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')

        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        self.textLabel  = QLabel('默认文本')
        self.imageLabel=QLabel()        # 创建用于显示图像的label
        self.imageLabel.setPixmap(QPixmap('./images/book1.png'))

        layout = QGridLayout()      # 使用栅格布局
        layout.addWidget(textCopyButton,0,0)
        layout.addWidget(imageCopyButton,0,1)
        layout.addWidget(htmlCopyButton,0,2)
        layout.addWidget(textPasteButton,1,0)
        layout.addWidget(htmlPasteButton,1,1)
        layout.addWidget(imagePasteButton,1,2)

        layout.addWidget(self.textLabel,2,0,1,2)
        layout.addWidget(self.imageLabel,2,2)

        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setWindowTitle('剪贴板演示')

    def copyText(self):
        clipboard = QApplication.clipboard()    # 获取剪切板对象
        clipboard.setText('hello world')        # 将文本复制到剪切板板上
    def pasteText(self):
        clipboard = QApplication.clipboard()        # 获取剪切板对象
        self.textLabel.setText(clipboard.text())        # 将剪切板上的文本复制到对应的空间上

    def copyImage(self):
        clipboard = QApplication.clipboard()        # 获取剪切板对象
        clipboard.setPixmap(QPixmap('./1.jpg'))       # 将图像复制到剪切板板上

    def pasteImage(self):
        clipboard = QApplication.clipboard()        # 获取剪切板对象
        self.imageLabel.setPixmap(clipboard.pixmap())       # 将剪切板上的图像复制到对应的空间上

    def copyHtml(self):
        mimeData = QMimeData()      # 得到剪切板内的数据类型
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)     # 将html代码复制到剪切板里

    def pasteHtml(self):
        clipboard = QApplication.clipboard()        # 获取剪切板
        mimeData = clipboard.mimeData()             # 获得数据类型
        if mimeData.hasHtml():                      # 如果数据为html类型，则继续处理
            self.textLabel.setText(mimeData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())

