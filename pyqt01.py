# import sys
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(500, 500)
#     w.move(600, 300)
#     w.setGeometry(600, 300, 500, 500)
#     # 上面setGeometry与resize和move的联合作用相同
#     w.setWindowTitle("李泓澔")
#     w.show()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('yeah')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
