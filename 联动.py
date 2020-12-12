import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_untitled
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_untitled.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
