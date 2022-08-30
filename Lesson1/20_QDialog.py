'''
对话框（QDialog）
    QMessageBox：显示消息对话框
    QColorDialog：显示颜色对话框
    QFileDialog：用来显示文件打开或者保存对话框的
    QFontDialog：用来显示字体对话框的
    QInputDialog：用来获取用户输入信息对话框

    QMainWindow
    QWidget
    QDialog

'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton(self)     # 传入self，直接把button放置在窗口上
        self.button.setText('弹出对话框')
        self.button.move(50,50)         # 将按钮移动到窗口的相应位置
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()      # 创建对话框的实例
        button = QPushButton('确定',dialog)       # 将控件放置在对话框内
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)   # 设置对话框以模式的状态显示，即给对话框显示时，窗口中其他的对话框皆不可用，除非关闭此对话框

        dialog.exec()       # 显示对话框

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
