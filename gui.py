from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import config as cg 
import sys
import os
from Buttons import buttons
from Grapics import grapics
import time
from database import database
from GenerateID import genID
from SerialComm import commDev
from datetime import datetime

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        self.db = database()
        self.db_state = self.db.db_state
        self.total_ids = self.db.totalIDs
        self.genID = genID()
        self.commDev = commDev()
        self.sc_state = self.commDev.sc_state
        self.cwd = os.getcwd()
        self.number = "0"
        self.state = "Main"
        
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.setGeometry(cg.window_x, cg.window_y, cg.width, cg.height)
        MainWindow.setEnabled(True)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.error_dialog = QtWidgets.QErrorMessage()
        
        self.grapics = grapics(self.centralwidget,self.cwd,self.commDev)
        self.buttons = buttons(self.centralwidget,self.cwd)
        self.connectServer()
        self.dbErrorWarning()
        self.actionExit = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'),MainWindow)
        self.actionExit.activated.connect(self.action_Exit)
        
        self.actionSwitch = QtWidgets.QShortcut(QtGui.QKeySequence('Space'),MainWindow)
        self.actionSwitch.activated.connect(self.action_Switch)
            
            
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.buttons.button1.clicked.connect(self.init_device)
        self.buttons.button2.clicked.connect(self.button2_click)
        self.buttons.button3.clicked.connect(self.button3_click)
        self.buttons.button4.clicked.connect(self.button4_click)
        self.buttons.button5.clicked.connect(self.button5_click)
        self.buttons.button6.clicked.connect(self.button6_click)
        self.buttons.button8.clicked.connect(self.button8_click)
        self.buttons.button9.clicked.connect(self.connectServer)

    def takeinputs(self):
        Number, ok = QtWidgets.QInputDialog.getText(
             self.centralwidget , 'SIM NUMBER', 'Enter Sim Number:')
        if ok:
            try:
                print(Number)
                self.number = str(Number)
            except IndexError:
                pass
        else:
            return False
        return self.number
    
    def duplicateNumber(self):
        Number, ok = QtWidgets.QInputDialog.getText(
             self.centralwidget , 'Duplicate SIM Error!', 'SIM already used! Enter New Sim Number:')
        if ok:
            try:
                self.number = str(Number)
                print(self.number)
            except IndexError:
                pass
        else:
            return False
        return self.number
    
    def invalidNumber(self):
        Number, ok = QtWidgets.QInputDialog.getText(
             self.centralwidget , 'Invalid SIM Error!', 'Invalid sim number! Enter New Sim Number:')
        if ok:
            try:
                self.number = str(Number)
                print(self.number)
            except IndexError:
                pass
        else:
            return False
        return self.number
    
    def dbErrorWarning(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("Could't establish connection \n with database")
        # self.msg.setInformativeText("Could't connect to database")
        self.msg.setWindowTitle("Connection failed")
        self.msg.setDetailedText("Remote server connection failed: contact your admin")
        
        
    def action_Switch(self):
        if self.state == "Main":
            self.button1_click()
        elif self.state == "showCommPorts":
            self.button8_click()
        
    def action_Exit(self):
        if self.state == "Settings":
            self.loadMain()
        elif self.state == "showCommPorts":
            self.goto_settings()
        elif self.state == "credits":
            self.goto_settings()
        else:
            # print("Going offline")
            # time.sleep(1)
            self.offline()
            print("Exiting...")
            time.sleep(1)
            # print("...")
            sys.exit()
        
    def goto_settings(self):
        if self.state == "Main":
            self.actionSwitch.disconnect()
            self.grapics.indicator.hide()
            self.buttons.button1.hide()
            self.buttons.button1.setEnabled(False)
            self.buttons.button2.hide()
            self.buttons.button2.setEnabled(False)
            self.buttons.button3.hide()
            self.buttons.button3.setEnabled(False)
            self.grapics.status.hide() 
            self.grapics.ring.hide()
            self.grapics.click_to.hide()
        elif self.state == "showCommPorts":
            self.actionSwitch.disconnect()
            self.grapics.showPorts.setEnabled(False)
            self.grapics.showPorts.hide()
            self.grapics.selectedPort.hide()
            self.grapics.selectedPort.hide()
            self.buttons.button8.hide()
            self.buttons.button8.setEnabled(False)
            self.grapics.click_to.hide()
        elif self.state == "credits":
            self.grapics.credits.hide()
            
        self.blur_effect = QtWidgets.QGraphicsBlurEffect() 
        self.grapics.background.setGraphicsEffect(self.blur_effect)
       
        self.buttons.button4.show()
        self.buttons.button4.setEnabled(True)
        self.buttons.button5.show()
        self.buttons.button5.setEnabled(True)
        self.buttons.button6.show()
        self.buttons.button6.setEnabled(True)
        self.buttons.button7.show()
        self.buttons.button7.setEnabled(True)
        
        self.state = "Settings"
           
    def loadMain(self):
        if self.commDev.commPort is not None:
                self.grapics.ring.setEnabled(True)
        self.blur_effect.setEnabled(False)
        self.grapics.indicator.show()
        self.buttons.button1.show()
        self.buttons.button1.setEnabled(True)
        self.buttons.button2.show()
        self.buttons.button2.setEnabled(True)
        self.buttons.button3.show()
        self.buttons.button3.setEnabled(True)
        self.buttons.button4.hide()
        self.buttons.button4.setEnabled(False)
        self.buttons.button5.hide()
        self.buttons.button5.setEnabled(False)
        self.buttons.button6.hide()
        self.buttons.button6.setEnabled(False)
        self.buttons.button7.hide()
        self.buttons.button7.setEnabled(False)
        self.actionSwitch.activated.connect(self.action_Switch)
        self.grapics.status.show()
        self.grapics.ring.show()
        self.grapics.click_to.show()
        self.grapics.click_to.setText("CLICK SPACE TO CONNECT")
        self.grapics.click_to.adjustSize()
        self.state = "Main"
    
    def gotoCommPorts(self):
        self.state = "showCommPorts"
        self.actionSwitch.activated.connect(self.action_Switch)
        self.buttons.button4.show()
        self.buttons.button4.setEnabled(True)
        self.buttons.button5.hide()
        self.buttons.button5.setEnabled(False)
        self.buttons.button6.hide()
        self.buttons.button6.setEnabled(False)
        self.buttons.button7.hide()
        self.buttons.button7.setEnabled(False)
        self.buttons.button8.show()
        self.buttons.button8.setEnabled(True)
        self.grapics.availablePorts()
        self.grapics.showPorts.show()
        self.grapics.connectedport()
        self.grapics.selectedPort.show()
        self.grapics.click_to.setText("CLICK SPACE TO SWITCH PORTS")
        self.grapics.click_to.show()
        self.grapics.click_to.adjustSize()

    def init_device(self):
        print("push button clikced")
        self.offline()
        while True:
            if self.takeinputs():
                if len(self.number) == 11:
                    print("correct number length")
                    self.offline()
                    self.commDev.auto_establish_comm()
                    if self.commDev.connectedPort is not None:
                        if self.commDev.sc_state == 1:
                            try:
                                nextID = self.db.getTotalID() + 1
                            except:
                                self.msg.show()
                                print("database didn't respond")
                                break
                            id_pass = self.genID.newID(nextID)
                            Id,pswd = id_pass[0],id_pass[1]
                            print("sending id",Id)
                            self.commDev.communicate(Id)
                            time.sleep(1)
                            if self.db.addNew(Id[4:], self.number, pswd, datetime.now()) is False:
                                print("Duplicate mobile number")
                                self.commDev.communication = 0
                                self.commDev.flush_device()
                                self.duplicateNumber()
                                continue
                        self.commDev.close_device()
                    if self.commDev.communication == 1:
                        self.online()
                        self.grapics.ring.setEnabled(True)
                    break
                else:
                    self.invalidNumber()
                    print("invalid number")
                    continue
                    
            else:
                break          
        
    def button2_click(self):  
        self.grapics.click_to.adjustSize()
        try:
            self.db.clearEntries(1)
            time.sleep(1)
        except:
            pass
            # print("Communication port already established")
               
    def button3_click(self):
        self.goto_settings()
    
    def button4_click(self):
        if self.state == "Settings":
            self.loadMain()
        elif self.state == "showCommPorts":
            self.goto_settings()
        elif self.state == "credits":
            self.goto_settings()
    
    def button6_click(self):
        self.gotoCommPorts()

    def button5_click(self):
        self.state = "credits"
        self.buttons.button4.show()
        self.buttons.button4.setEnabled(True)
        self.buttons.button5.hide()
        self.buttons.button5.setEnabled(False)
        self.buttons.button6.hide()
        self.buttons.button6.setEnabled(False)
        self.buttons.button7.hide()
        self.buttons.button7.setEnabled(False)
        self.grapics.showCredits()
        self.grapics.credits.show()
    
    def button8_click(self):
        # self.offline()
        # self.commDev.change_comPort()
        # self.grapics.click_to.setText("CLICK SPACE TO SWITCH PORTS")
        # self.grapics.click_to.show()
        # self.grapics.click_to.adjustSize()
        # self.grapics.selectedPort.setText("CONNECTED PORT:"+str(self.commDev.connectedPort).upper())
        # self.grapics.showPorts.setText("AVAILABLE PORTS:\n"+str(self.commDev.find_com_port()).upper())
        # self.grapics.selectedPort.adjustSize()
        # self.grapics.showPorts.adjustSize()
        # if self.commDev.connectedPort is None:
        #     self.grapics.ring.setEnabled(False)
        pass

    def online(self):
        # time.sleep(1)
        self.grapics.status.setText("<font color=\"white\">NEW DEVICE INITIATED</font>")
        self.grapics.status.adjustSize() 
        self.grapics.click_to.setText("CLICK SPACE TO CONNECT")
        self.grapics.click_to.adjustSize()
        self.grapics.indicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.green_indicator))
        
    def offline(self):
        # self.state_data = "off"
        # if self.commDev.sc_state == 1:
        #     if self.commDev.communicate(self.state_data) == False:
        #         self.grapics.ring.setEnabled(False)
        self.grapics.ring.setEnabled(False)
        # self.grapics.status.setText("STATUS  <font color=\"red\"> OFF </font> ")
        self.grapics.status.adjustSize() 
        self.grapics.click_to.setText("CLICK SPACE TO CONNECT")
        self.grapics.indicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.red_indicator))
        
    def connectServer(self):
        print("trying to reconnect server")
        if self.db_state == 0:
            if self.db.connectDB():
                self.db_state = 1
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.serverOnline), QtGui.QIcon.Active, QtGui.QIcon.On)
                self.buttons.button9.setIcon(icon)
            else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.reconnectServer), QtGui.QIcon.Active, QtGui.QIcon.On)
                self.buttons.button9.setIcon(icon)
        else:
            print("server Connection extablished successfully") 
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.serverOnline), QtGui.QIcon.Active, QtGui.QIcon.On)
            self.buttons.button9.setIcon(icon)     
        
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.showNormal()
    sys.exit(app.exec_())
