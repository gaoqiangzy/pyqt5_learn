from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--记得好看点')


        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 800, 1270)

        self.bt1 = QPushButton('打开文件',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('选择字体',self)
        self.bt2.move(350,70)
        self.bt3 = QPushButton('选择颜色',self)
        self.bt3.move(350,120)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)

        self.show()
    def openfile(self):
        # getOpenFileName（）方法中的第一个字符串是标题。第二个字符串指定对话框工作目录。默认情况下，文件过滤器设置为所有文件（*），即不限制打开文件的类型。
        # 如果增加文件过滤，可以改成如下语句：fname = QFileDialog.getOpenFileName(self, '打开文件','./',("Images (*.png *.xpm *.jpg)"))
        fname = QFileDialog.getOpenFileName(self, '打开文件','./')
        if fname[0]:
            with open(fname[0], 'r',encoding='utf8',errors='ignore') as f:
                self.tx.setText(f.read())
    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)
    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())