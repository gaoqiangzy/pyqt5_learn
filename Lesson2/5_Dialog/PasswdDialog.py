#coding=utf-8
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator

class PasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350,100)
        self.setWindowTitle("密码输入框")

        self.lb = QLabel("请输入密码：",self)
        
        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)
        
        self.bt1 = QPushButton("确定",self)
        self.bt2 = QPushButton("取消",self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        # 屏蔽了鼠标右键、禁用复制、粘贴快捷键、鼠标在密码框中不可移动，不可全选
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText("密码不超15位，只能有数字和字母，必须以字母开头")
        # 限定输入框显示信息的方式，这里设置密码方式，显示黑点
        """其他设置：
            .Normal:显示输入的字符
            .NoEcho:不显示任何东西
            .Password:显示与系统相关的密码掩码
            .PasswordEchoOnEdit:在编辑时输入时显示字符，否则用密码显示字符
        """
        self.edit.setEchoMode(QLineEdit.Password)

        
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validator)

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)
        
        object = QObject()
        
    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)#继续传递该事件到被观察者，由其本身调用相应的事件
        
    def Ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            self.done(1)          # 结束对话框返回1
    
    def Cancel(self):
        self.done(0)          # 结束对话框返回0
    