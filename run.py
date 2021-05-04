if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import gui
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    if len(sys.argv) > 1:
        ui.setupUi(MainWindow, sys.argv[1])
    else:
        ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    