

# 多线程更新UI数据（在两个线程中传递数据）
# 在多个线程中，利用信号与槽互相传递数据
# 即：另外一个线程不断的向主线程来发送信号



from PyQt5.QtCore import QThread ,  pyqtSignal,  QDateTime
from PyQt5.QtWidgets import QApplication,  QDialog,  QLineEdit
import time
import sys


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))     # 传递参数
            time.sleep(1)
class ThreadUpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400,100)
        self.input = QLineEdit(self)
        self.input.resize(400,100)

        self.initUI()
    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()        # 启动线程

    def handleDisplay(self,data):
        self.input.setText(data)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ThreadUpdateUI()
    example.show()
    sys.exit(app.exec_())

