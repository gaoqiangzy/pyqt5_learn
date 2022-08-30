

# 栅格布局：表单设计



import sys,math
from PyQt5.QtWidgets import *


class GridForm(QWidget) :
    def __init__(self):
        super(GridForm,self).__init__()
        self.setWindowTitle("栅格布局：表单设计")

        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)     # 设置控件的间距

        grid.addWidget(titleLabel,0,0)
        grid.addWidget(titleEdit,0,1)

        grid.addWidget(authorLabel,1,0)
        grid.addWidget(authorEdit,1,1)

        grid.addWidget(contentLabel,2,0)
        grid.addWidget(contentEdit,2,1,5,1)

        self.setLayout(grid)
        self.resize(350,300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GridForm()
    main.show()
    sys.exit(app.exec_())

