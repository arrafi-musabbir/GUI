if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import gui
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow, sys.argv[1])
    MainWindow.show()
    sys.exit(app.exec_())
    