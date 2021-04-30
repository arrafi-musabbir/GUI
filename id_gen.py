
from PyQt5 import QtCore, QtGui, QtWidgets
from serialID import genId


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.id = genId()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(400, 200, 400, 800)
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(24)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 140, 401, 291))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.button1_click)

    def button1_click(self):
        self.id.communicate()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CONNECT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
