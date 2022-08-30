
# 为树节点添加响应事件

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class TreeEvent(QMainWindow):
    def __init__(self, parent=None):
        super(TreeEvent, self).__init__(parent)
        self.setWindowTitle('为树节点添加响应事件')

        self.tree = QTreeWidget()       # 创建树控件

        self.tree.setColumnCount(2)     # 为树控件指定列数

        self.tree.setHeaderLabels(['Key','Value'])      # 设置树的头标签

        root  = QTreeWidgetItem(self.tree)          # 创建树的根节点
        root.setText(0,'root')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)          # 给根节点创建第一个子节点
        child1.setText(0,'child1')
        child1.setText(1,'1')

        child2 = QTreeWidgetItem(root)          # 给根节点创建第二个子节点
        child2.setText(0,'child2')
        child2.setText(1,'2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'child3')
        child3.setText(1,'3')
        self.tree.clicked.connect(self.onTreeClicked)       # 给树控件绑定点击事件

        self.setCentralWidget(self.tree)        # 把树控件设置为中心控件
    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0),item.text(1)))          # item.text(0)：获得节点值；item.text(1)：获得value值

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeEvent()
    tree.show()
    sys.exit(app.exec_())

