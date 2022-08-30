from PyQt5.QtWidgets  import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from MySharedObject  import MySharedObject
from PyQt5.QtWebChannel import  QWebChannel
import sys
import os



# JavaScript调用Python函数计算阶乘
#
# 将Python的一个对象映射到JavaScript中
#
# 将槽函数映射到JavaScript中



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
from factorial import *

channel = QWebChannel()     # pyqt5中的
factorial = Factorial()
class PyFactorial(QWidget):

    def __init__(self):
        super(PyFactorial, self).__init__()
        self.setWindowTitle('Python计算阶乘')
        self.resize(600,300)
        layout=QVBoxLayout()

        self.browser = QWebEngineView()     # 创建Web浏览器控件
        url = os.getcwd() + '/f.html'
        self.browser.load(QUrl.fromLocalFile(url))      # 装载html
        channel.registerObject("obj",factorial)         # 注册对象  第一个参数是字符串，第二个参数是实际映射的对象
        self.browser.page().setWebChannel(channel)          # 将channel设置到Web浏览器控件上

        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyFactorial()
    win.show()
    sys.exit(app.exec_())
