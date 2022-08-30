
"""
QLbael控件：
setAligment()：设置文本的对其方式
setIndent()：设置文本缩进
text():     获取文本内容
setBuddy()：设置伙伴关系
setText()：  设置文本内容
selectedText()：返回所选择的字符
setWordWrap()：设置是否允许换行

QLabel常用信号（事件）：
1、当鼠标滑过QLabel控件时触发：linkHovered
2、当鼠标单击QLabel控件时触发：linkActivated

"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QVBoxLayout,QWidget,QLabel       # QMainWindow:主窗口;QApplication:创建应用程序 ;QDesktopWidget:用于获取桌面信息参数
from PyQt5.QtGui import QIcon           # 用来添加图标
from PyQt5.QtGui import QFont           # 设置字体
from PyQt5.QtGui import QPalette        # 调试版，设置背景色的
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap         # 用于显示图片

class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo,self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)       # QLbael控件
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签。</font>")       # 为第一个label设置文本
        label1.setAutoFillBackground(True)      # 设置自动填充背景

        paltette = QPalette()    # 创建调试板
        paltette.setColor(QPalette.Window,Qt.blue)       # 设置颜色

        label1.setPalette(paltette) # 对lebel使用调试板
        label1.setAlignment(Qt.AlignCenter)     # 设置文本居中对齐

        label2.setText("<a href='#'>欢迎使用Python  GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("./1.jpg"))        # 设置图片

        label4.setOpenExternalLinks(True)       # 如果设为True，用浏览器打开网页；如果设为False，调用槽函数
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《这本书》</a>")
        label4.setAlignment(Qt.AlignRight)  # 设置文本右对齐
        label4.setToolTip("这是一个超级链接")
        # 使用垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # 绑定相应事件
        label2.linkHovered.connect(self.linkHovered)
        label2.linkActivated.connect(self.linkclicked)

        self.setLayout(vbox)    # 设置布局
        self.setWindowTitle("QLabel控件演示")

    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发事件")
    def linkclicked(self):
        print("当鼠标单击label4标签时，触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/Dragon.ico"))     # 设置应用程序的图标
    main_ = QLabelDemo()
    main_.show()
    sys.exit(app.exec())
