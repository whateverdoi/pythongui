# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lhh/文档/GUI/pyqt重新学/translate.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 440, 801, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("font: 36pt \"Sans Serif\";\n"
                                        "background-color: rgb(81, 223, 29);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("font: 36pt \"Sans Serif\";\n"
                                      "background-color: rgb(214, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setStyleSheet("font: 36pt \"Sans Serif\";\n"
                                        "background-color: rgb(214, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet("font: 36pt \"Sans Serif\";\n"
                                        "background-color: rgb(255, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(220, 520, 361, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setStyleSheet("font: 15pt \"Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setStyleSheet("font: 15pt \"Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(4, 24, 791, 421))
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setStyleSheet("font: 20pt \"Sans Serif\";\n"
                                 "")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget2)
        self.label_5.setStyleSheet("font: 20pt \"Sans Serif\";\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget2)
        self.textEdit.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget2)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 146, 119);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actiond = QtWidgets.QAction(MainWindow)
        self.actiond.setObjectName("actiond")
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "翻译"))
        self.pushButton.setText(_translate("MainWindow", "清除"))
        self.pushButton_4.setText(_translate("MainWindow", "清除"))
        self.pushButton_3.setText(_translate("MainWindow", "复制"))
        self.label_2.setText(_translate("MainWindow", "作者：为空"))
        self.label_3.setText(_translate("MainWindow", "制作日期：2020.12.12"))
        self.label.setText(_translate("MainWindow", "请在下面输入文本"))
        self.label_5.setText(_translate("MainWindow", "翻译结果"))
        self.menu.setTitle(_translate("MainWindow", "退出"))
        self.action.setText(_translate("MainWindow", "退出"))
        self.action_2.setText(_translate("MainWindow", "交代哦"))
        self.actiond.setText(_translate("MainWindow", "d按时"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
