from PyQt5.QtCore import *
class Factorial(QObject):
    @pyqtSlot(int, result=int)      # 定义槽函数，需要传入参数的话，则标明传入参数类型；需要返回结果的话，则通过命名参数指明返回结果
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.factorial(n - 1) * n


if __name__ == '__main__':
    factorial = Factorial()
    print(factorial.factorial(99))

