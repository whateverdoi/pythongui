'''
设置了退出询问
'''
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('message box')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message', "are you really want to quit", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('你好')
        self.setGeometry(300, 300, 500, 500)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message', "do you really want to quit?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
