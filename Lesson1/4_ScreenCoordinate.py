import sys
# QMainWindow:主窗口;QApplication:创建应用程序;QHBoxLayout:水平布局;QWidget:控件;   QPushButton:button对象类
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon  # 用来添加图标


def onClick_button():
    print("1")
    print("widget.x()=%d" % (widget.x()))       # 250 窗口横坐标
    print("widget.y()=%d" % (widget.y()))       # 200  窗口纵坐标  含有顶部边框（即包含标签栏）
    print("widget.width()=%d" % (widget.width()))      # 300   工作区的宽度
    print("widget.height()=%d" % (widget.height()))     # 240   工作区的高度

    print("2")
    print("widget.geometry().x()=%d" % (widget.geometry().x()))
    print("widget.geometry().y()=%d" % (widget.geometry().y()))     # 不含有顶部边框（即不包含标签栏）
    print("widget.geometry().width()=%d" % (widget.geometry().width()))
    print("widget.geometry().height()=%d" % (widget.geometry().height()))

    print("3")
    print("widget.frameGeometry().x()=%d" % (widget.frameGeometry().x()))
    print("widget.frameGeometry().y()=%d" % (widget.frameGeometry().y()))  # 不含有顶部边框（即不包含标签栏）
    print("widget.frameGeometry().width()=%d" % (widget.frameGeometry().width()))
    print("widget.frameGeometry().height()=%d" % (widget.frameGeometry().height()))

app = QApplication(sys.argv)
widget = QWidget()  # 创建窗口
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_button)  # 绑定事件

btn.move(24, 52)  # 将按钮移动到相应的位置

widget.resize(300, 240)         # 设置的是工作区的尺寸
widget.move(250, 200)  # 移动窗口

widget.setWindowTitle("屏幕坐标系")
widget.show()
sys.exit(app.exec_())
