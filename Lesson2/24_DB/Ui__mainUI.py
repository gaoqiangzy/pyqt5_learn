# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\PyQt5\source_code_for_pyqt5_tutorials\PyQt561\_mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_11.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_11.addWidget(self.comboBox)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.pushButton_search = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_12.addWidget(self.pushButton_search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/book.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.label_country = QtWidgets.QLabel(self.groupBox)
        self.label_country.setText("")
        self.label_country.setObjectName("label_country")
        self.horizontalLayout_9.addWidget(self.label_country)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_isbn = QtWidgets.QLabel(self.groupBox)
        self.label_isbn.setText("")
        self.label_isbn.setObjectName("label_isbn")
        self.horizontalLayout.addWidget(self.label_isbn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.label_bookname = QtWidgets.QLabel(self.groupBox)
        self.label_bookname.setText("")
        self.label_bookname.setObjectName("label_bookname")
        self.horizontalLayout_2.addWidget(self.label_bookname)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_author = QtWidgets.QLabel(self.groupBox)
        self.label_author.setText("")
        self.label_author.setObjectName("label_author")
        self.horizontalLayout_3.addWidget(self.label_author)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_classification = QtWidgets.QLabel(self.groupBox)
        self.label_classification.setText("")
        self.label_classification.setObjectName("label_classification")
        self.horizontalLayout_4.addWidget(self.label_classification)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_publisher = QtWidgets.QLabel(self.groupBox)
        self.label_publisher.setText("")
        self.label_publisher.setObjectName("label_publisher")
        self.horizontalLayout_5.addWidget(self.label_publisher)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_pages = QtWidgets.QLabel(self.groupBox)
        self.label_pages.setText("")
        self.label_pages.setObjectName("label_pages")
        self.horizontalLayout_6.addWidget(self.label_pages)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_pubdate = QtWidgets.QLabel(self.groupBox)
        self.label_pubdate.setText("")
        self.label_pubdate.setObjectName("label_pubdate")
        self.horizontalLayout_7.addWidget(self.label_pubdate)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.label_price = QtWidgets.QLabel(self.groupBox)
        self.label_price.setText("")
        self.label_price.setObjectName("label_price")
        self.horizontalLayout_8.addWidget(self.label_price)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_createbook = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_createbook.setObjectName("pushButton_createbook")
        self.horizontalLayout_10.addWidget(self.pushButton_createbook)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信公众号：学点编程吧--极简图书管理Plus"))
        self.pushButton_search.setText(_translate("MainWindow", "搜索"))
        self.tableView.setStatusTip(_translate("MainWindow", "双击表格修改数据"))
        self.groupBox.setTitle(_translate("MainWindow", "更多图书信息"))
        self.label_5.setText(_translate("MainWindow", "国    家"))
        self.label_2.setText(_translate("MainWindow", "I S B N"))
        self.label_15.setText(_translate("MainWindow", "书    名"))
        self.label_4.setText(_translate("MainWindow", "作    者"))
        self.label_3.setText(_translate("MainWindow", "图书分类"))
        self.label_6.setText(_translate("MainWindow", "出版单位"))
        self.label_10.setText(_translate("MainWindow", "页    数"))
        self.label_8.setText(_translate("MainWindow", "出版年份"))
        self.label_12.setText(_translate("MainWindow", "定    价"))
        self.label_14.setText(_translate("MainWindow", "内容简介"))
        self.pushButton_createbook.setText(_translate("MainWindow", "新建图书档案..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
