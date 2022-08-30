'''
计数器控件（QSpinBox）
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块演示')
        self.resize(300, 700)
        self.setWindowIcon(QIcon('./images/doc.ico'))
        layout = QVBoxLayout()  # 使用垂直布局

        self.label = QLabel("你好，PyQt5")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        """创建水平的滑块"""
        self.slider=QSlider(Qt.Horizontal)      # 设置水平的滑块
        # 设置最小值
        self.slider.setMinimum(12)      # 设置最小值
        # 设置最大值
        self.slider.setMaximum(48)      # 设置最大值
        # 步长
        self.slider.setSingleStep(3)     # 设置步长
        # 设置当前值
        self.slider.setValue(18)            # 设置当前值
        # 设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)     # QSlider.TicksBelow：刻度在下方
        # 设置刻度的间隔
        self.slider.setTickInterval(6)

        """创建竖直的滑块"""
        self.slider2 = QSlider(Qt.Vertical)  # 创建垂直的滑块
        # 设置最小值
        self.slider2.setMinimum(12)  # 设置最小值
        # 设置最大值
        self.slider2.setMaximum(48)  # 设置最大值
        # 步长
        self.slider2.setSingleStep(3)  # 设置步长
        # 设置当前值
        self.slider2.setValue(18)  # 设置当前值
        # 设置刻度的位置，刻度在下方
        self.slider2.setTickPosition(QSlider.TicksLeft)  # QSlider.TicksBelow：刻度在下方
        # 设置刻度的间隔
        self.slider2.setTickInterval(6)

        layout.addWidget(self.slider)
        layout.addWidget(self.slider2)

        self.slider.valueChanged.connect(self.valueChange)      # 进行信号的绑定
        self.slider2.valueChanged.connect(self.valueChange)  # 进行信号的绑定
        self.setLayout(layout)

    def valueChange(self):
        print("当前值：%s"%(self.sender().value()))       # 输出当前值
        size=self.sender().value()
        self.label.setFont(QFont("Arial",size))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())
