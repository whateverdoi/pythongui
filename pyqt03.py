'''
设置了应用图标
设置了按钮部件
设置了位置（这是废话）

'''
import sys
from PyQt5.QtWidgets import(QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import(QFont, QIcon)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 20))
        self.setToolTip('This is a <b>Qwidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>Qpushbutton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(125, 75)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('web3.jpeg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
