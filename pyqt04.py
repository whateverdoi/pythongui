'''
设置了一个退出按钮
'''
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.move(80, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('QUIT instance')
w.setGeometry(300, 300, 250, 200)
w.setWindowIcon(QIcon('web.png'))
qbtn = QPushButton('QUIT', w)
qbtn.resize(qbtn.sizeHint())
qbtn.move(50, 50)
qbtn.clicked.connect(QCoreApplication.instance().quit)
w.show()
sys.exit(app.exec_())


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('你好吗')
        self.setGeometry(500, 500, 400, 400)
        self.setWindowIcon(QIcon('web2.png'))
        qbtn = QPushButton('QUIT', self)
        qbtn.setGeometry(50, 50, 50, 50)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
