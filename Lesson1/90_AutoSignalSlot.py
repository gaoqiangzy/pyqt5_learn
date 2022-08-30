
# 信号与槽自动连接
#
# on_objectname_signalname
#
# on_okButton_clicked



from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication ,QWidget ,QHBoxLayout , QPushButton
import sys

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot,self).__init__()
        self.okButton = QPushButton("ok",self)
        self.okButton.setObjectName("okButton")     # 给按钮控件设置一名称
        self.okButton1 = QPushButton("cancel",self)
        self.okButton1.setObjectName("cancelButton")


        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)     #1、按照相应的规则使得信号与槽自动连接
        #self.okButton.clicked.connect(self.on_okButton_clicked)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):  # 2、将槽函数使用@QtCore.pyqtSlot()注释一下
        print("点击了ok按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancel按钮")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = AutoSignalSlot()
    example.show()
    sys.exit(app.exec_())

