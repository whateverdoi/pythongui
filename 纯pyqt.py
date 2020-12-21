import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    w.resize(1000, 500)
    w.move(300, 300)
    w.setWindowTitle("李泓澔")
    w.show()
    sys.exit(app.exec_())
