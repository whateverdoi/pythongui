import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()  # 目的是为了继承qwidget这个父类的属性

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 420)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web3.jpeg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# 上面是面向对象过程,下面面向对象
app = QApplication(sys.argv)
w = QWidget()
w.resize(500, 420)
w.move(300, 300)
w.setWindowTitle('Icon')
w.setWindowIcon(QIcon('web1.png'))
w.show()
sys.exit(app.exec_())
