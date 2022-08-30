
# 树控件（QTreeWidget）的基本用法

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class BasicTreeWidget(QMainWindow):
    def __init__(self, parent=None):
        super(BasicTreeWidget, self).__init__(parent)
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')

        self.tree = QTreeWidget()       # 创建树控件
        # 为树控件指定列数
        self.tree.setColumnCount(2)     # 为树控件指定列数

        # 指定列标签
        self.tree.setHeaderLabels(['Key','Value'])      # 指定列标签

        root = QTreeWidgetItem(self.tree)           # 将根节点放置到tree上
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('./images/root.png'))

        self.tree.setColumnWidth(0,160)     # 即给第一列设置列宽

        # 添加子节点1
        child1 = QTreeWidgetItem(root)          # 给根节点添加子节点
        child1.setText(0,'子节点1')                # 设置第一列文本
        child1.setText(1,'子节点1的数据')             # 设置第二列文本
        child1.setIcon(0,QIcon('./images/bao3.png'))
        child1.setCheckState(0,Qt.Checked)          # 给节点添加复选框


        # 添加子节点2
        child2 = QTreeWidgetItem(root)          # 表示将第二个子节点添加到根节点
        child2.setText(0,'子节点2')
        child2.setIcon(0,QIcon('./images/bao6.png'))

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'子节点2-1')
        child3.setText(1,'新的值')
        child3.setIcon(0,QIcon('./images/music.png'))


        self.tree.expandAll()       # 设置所有节点默认为打开状态

        self.setCentralWidget(self.tree)        # 使其作为中心控件充满整个屏幕


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = BasicTreeWidget()
    tree.show()
    sys.exit(app.exec_())

