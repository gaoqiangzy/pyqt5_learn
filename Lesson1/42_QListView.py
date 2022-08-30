'''
显示列表数据（QListView控件）
'''
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import sys


class ListViewDemo(QWidget):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(300, 270)
        layout = QVBoxLayout()

        listview = QListView()      # 创建QListView控件
        listModel = QStringListModel()      # 创建字符串列表模型
        self.list = ["列表项1","列表项2", "列表项3"]         # 数据源

        listModel.setStringList(self.list)      # 将模型与列表数据源相关联

        listview.setModel(listModel)        # 将模型与控件关联
        listview.clicked.connect(self.clicked)      # 绑定控件单击事件
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,"QListView","您选择了：" + self.list[item.row()])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())
