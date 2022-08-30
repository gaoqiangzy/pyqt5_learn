'''
QTextEdit综合案例

'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon  # 用来添加图标
import sys


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('使用QTextEdit输入多行文本')
        self.setWindowIcon(QIcon('./images/doc.ico'))
        self.resize(300, 280)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton("显示文本")
        self.buttonHTML = QPushButton("显示HTML")

        self.buttonGetText = QPushButton("获取文本")
        self.buttonGetHTML = QPushButton("获取HTML")

        layout = QVBoxLayout()  # 创建垂直布局
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonGetText)
        layout.addWidget(self.buttonGetHTML)

        # 设置布局
        self.setLayout(layout)

        # 绑定事件
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonGetText.clicked.connect(self.onClick_ButtonGetText)
        self.buttonGetHTML.clicked.connect(self.onClick_ButtonGetHtml)

    def onClick_ButtonText(self):
        self.textEdit.setPlainText("Hello World，世界你好吗")

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color="blue" size="5">hello world</font>')

    def onClick_ButtonGetText(self):
        print(self.textEdit.toPlainText())  # 获取多行文本框内的文字内容

    def onClick_ButtonGetHtml(self):
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())
