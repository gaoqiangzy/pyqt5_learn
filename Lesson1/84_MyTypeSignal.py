
# 自定义信号
# pyqtSignal()    ：自定义对象



from PyQt5.QtCore import *

class MyTypeSignal(QObject):
    # 定义一个信号
    sendmsg=pyqtSignal(object)

    # 定义一个run方法，通过调用run方法来触发事件
    def run(self):
        self.sendmsg.emit("Hello pyqt5")    # 给槽函数传递参数

class Myslot(QObject):
    def get(self,msg):
        print("信息:"+msg)

if __name__ == '__main__':
    send = MyTypeSignal()
    slot = Myslot()
    send.sendmsg.connect(slot.get)      # 绑定槽函数
    send.run()

    send.sendmsg.disconnect(slot.get)       # 解绑槽函数
    send.run()

