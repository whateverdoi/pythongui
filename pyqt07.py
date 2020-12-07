'''
链接了一个滑动线和数字

'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QDesktopWidget)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(sld)
        vbox.addWidget(lcd)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300, 200, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


class Example(QWidget):
    def __init__(self):
        super().__init__()  # 继承父类，父类是QWideget
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(2, self)  # 里面的数字是用来设置字号的
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setWindowTitle('VBOX')
        self.resize(500, 500)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
