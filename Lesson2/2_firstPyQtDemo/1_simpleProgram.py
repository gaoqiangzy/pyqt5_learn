# 最基本的windows窗口
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # sys.argv参数是来自命令行的参数列表，写了这句话就能让我们的程序从命令行启动。
    app = QApplication(sys.argv)
    # QWidget小部件是PyQt5中所有用户界面对象的基类
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('窗口名称')
    w.show()
    # sys.exit（）方法确保一个干净的退出。
    sys.exit(app.exec_())