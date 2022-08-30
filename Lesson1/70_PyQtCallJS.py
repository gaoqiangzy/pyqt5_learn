
# PyQt5调用JavaScript代码
# PyQt5和JavaScript交互
#
# 什么叫交互
#
# PyQt5 <-> JavaScript


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os


class PyQtCallJS(QWidget):

    def __init__(self):
        super(PyQtCallJS, self).__init__()
        self.setWindowTitle('PyQt5调用JavaScript')
        self.setGeometry(5, 30, 1355, 730)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.browser = QWebEngineView()     # 创建web浏览器控件

        url = os.getcwd() + '/70.html'
        self.browser.load(QUrl.fromLocalFile(url))          # 装载本地的html页面

        self.layout.addWidget(self.browser)

        button = QPushButton('设置全名')
        button.clicked.connect(self.fullname)
        self.layout.addWidget(button)

    def js_callback(self,result):
        print(result)
    def fullname(self):
        self.value = 'hello world'
        self.browser.page().runJavaScript('fullname_function_name("' + self.value + '");',self.js_callback)           # self.js_callback为一个回调函数，即javaScript返回的值
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyQtCallJS()
    win.show()
    sys.exit(app.exec_())

