from PyQt5 import QtCore, QtGui, QtWidgets
import config as cg 

class grapics:
    
    def __init__(self,cw,cwd,sc):
        self.commDev = sc
        self.serial = 0
        self.centralwidget = cw
        self.cwd = cwd
        self.backGround()
        self.indiCator()
        self.staTus()
        self.green_ring()
        self.clickTo()
        self.dbErrorWarning()
        self.noCommWarning()
        self.internetConnection()
        self.noInternetWarning()
        self.invalidNumber()
        
    
    def backGround(self):
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, cg.width, cg.height))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.background.setFont(font)
        self.background.setAutoFillBackground(False)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.background))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
                      
    def indiCator(self):
        
        self.indicator = QtWidgets.QLabel(self.centralwidget)
        self.indicator.setGeometry(QtCore.QRect(cg.indicator_x,cg.indicator_y, cg.indicator_width, cg.indicator_height))
        self.indicator.setText("")
        self.indicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.red_indicator))
        self.indicator.setScaledContents(True)
        self.indicator.setObjectName("indicator")
        self.indicator.show()
        
    def staTus(self):
        
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(cg.width//4.5, cg.height//1.6, 11, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.status.setText("NO DEVICE CONNECTED <font color=\"red\"> </font> ")
        self.status.setFont(font)
        self.status.setStyleSheet("color:rgb(255, 255, 255)")
        self.status.setScaledContents(True)
        self.status.setObjectName("status")
        self.status.adjustSize()

    def green_ring(self):
        self.ring = QtWidgets.QLabel(self.centralwidget)
        self.ring.setGeometry(QtCore.QRect(cg.button1_x-5, cg.button1_y-5 , 130, 130))
        self.ring.setText(" ")
        self.ring.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.green_ring))
        self.ring.setScaledContents(True)
        self.ring.setObjectName("rign")
        self.ring.setEnabled(False)

    def internetConnection(self):
        self.netConnection = QtWidgets.QLabel(self.centralwidget)
        self.netConnection.setGeometry(QtCore.QRect(cg.button9_x+50, cg.button9_y-5, cg.button9_width+5, cg.button9_height+8))
        self.netConnection.setText(" ")
        self.netConnection.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.no_internet))
        self.netConnection.setScaledContents(True)
        self.netConnection.setObjectName("rign")
        self.netConnection.setEnabled(True)

    def noInternetWarning(self):
        self.noInternetmsg = QtWidgets.QMessageBox()
        self.noInternetmsg.setIcon(QtWidgets.QMessageBox.Warning)
        self.noInternetmsg.setText("No stable internet connection")
        # self.noInternetmsg.setInformativeText("Could't connect to database")
        self.noInternetmsg.setWindowTitle("Internet connection failed")
        self.noInternetmsg.setDetailedText("Can't establish stable internet connection: check if you internet connection source is working")
    
    def clickTo(self):
        self.click_to = QtWidgets.QLabel(self.centralwidget)
        self.click_to.setGeometry(QtCore.QRect(cg.width//2.9, cg.height-cg.height//3.5, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setWeight(75)
        self.click_to.setFont(font)
        self.click_to.setText("CLICK SPACE TO CONNECT")
        self.click_to.setStyleSheet("color:rgb(255, 255, 255)")
        self.click_to.setObjectName("click_to")
        self.click_to.setAlignment(QtCore.Qt.AlignCenter)
        self.click_to.adjustSize()

    def connectedport(self):
        self.port = str(self.commDev.commPort).upper()
        self.selectedPort = QtWidgets.QLabel(self.centralwidget)
        self.selectedPort.setGeometry(QtCore.QRect(cg.width//2.8, cg.height//1.4 - 40, 10, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setWeight(75)
        self.selectedPort.setText("CONNECTED PORT:"+self.port)
        self.selectedPort.setFont(font)
        self.selectedPort.setStyleSheet("color:rgb(255, 255, 0)")
        self.selectedPort.setScaledContents(True)
        self.selectedPort.setObjectName("selectedPort")
        self.selectedPort.hide()
        self.selectedPort.adjustSize()

    def availablePorts(self):
        self.ports = self.commDev.find_com_port()
        self.showPorts = QtWidgets.QLabel(self.centralwidget)
        self.showPorts.setGeometry(QtCore.QRect(cg.width//2.3, cg.height//2.3,  cg.button6_width, cg.button6_height))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.showPorts.setFont(font)
        self.showPorts.setStyleSheet("color:rgb(255, 255, 255)")
        self.showPorts.setText("AVAILABLE PORTS:\n" +str(self.ports).upper())
        self.showPorts.setAlignment(QtCore.Qt.AlignCenter)
        if self.ports is None:
            self.showPorts.setText("AVAILABLE PORTS:\n"+" "+"NONE")
        self.showPorts.adjustSize()
        self.showPorts.hide()
        self.showPorts.setObjectName("showPorts")
        
    def portIndiCator(self):
        self.portIndicator = QtWidgets.QLabel(self.centralwidget)
        self.portIndicator.setGeometry(QtCore.QRect(cg.width-50, 20, 25,25))
        self.portIndicator.setText("")
        self.portIndicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.noUsb))
        self.portIndicator.setScaledContents(True)
        self.portIndicator.setObjectName("portIndicator")

    def showCredits(self):
        self.credits = QtWidgets.QLabel(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(cg.width//5, cg.height/2, 11, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        name = "DATASOFT MANUFACTURING & ASSEMBLY"
        # email = "musabbir.arrafi@gmail.com"
        self.credits.setText(name)
        self.credits.setFont(font)
        self.credits.setStyleSheet("color:rgb(255, 255, 255)")
        self.credits.setScaledContents(True)
        # self.credits.setStyleSheet("QLabel { background-color : black;color:rgb(255, 255, 255)}")
        self.credits.setObjectName("credits")
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.credits.adjustSize()
        
    def dbErrorWarning(self):
        self.dbmsg = QtWidgets.QMessageBox()
        self.dbmsg.setIcon(QtWidgets.QMessageBox.Warning)
        self.dbmsg.setText("Could't establish connection \n with database")
        # self.msg.setInformativeText("Could't connect to database")
        self.dbmsg.setWindowTitle("Server connection failed")
        self.dbmsg.setDetailedText("Remote server connection failed: contact your admin")
        
    def noCommWarning(self):
        self.noCommmsg = QtWidgets.QMessageBox()
        self.noCommmsg.setIcon(QtWidgets.QMessageBox.Warning)
        self.noCommmsg.setText("No communication port found")
        # self.noCommmsg.setInformativeText("Could't connect to database")
        self.noCommmsg.setWindowTitle("Serial communication failed")
        self.noCommmsg.setDetailedText("Can't communicate with a device: check if the device is connected properly")
    
    def invalidNumber(self):
        self.invNum = QtWidgets.QLabel(self.centralwidget)
        self.invNum.setGeometry(QtCore.QRect(cg.width//2, cg.height//1.1, 11, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        name = "Invalid Number"
        # email = "musabbir.arrafi@gmail.com"
        self.invNum.setText(name)
        self.invNum.setFont(font)
        self.invNum.setStyleSheet("color:rgb(255, 255, 255)")
        self.invNum.setScaledContents(True)
        # self.credits.setStyleSheet("QLabel { background-color : black;color:rgb(255, 255, 255)}")
        self.invNum.setObjectName("invNum")
        self.invNum.setAlignment(QtCore.Qt.AlignCenter)
        self.invNum.adjustSize()
        self.invNum.show()