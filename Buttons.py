from PyQt5 import QtCore, QtGui, QtWidgets
import config as cg


class buttons:
    
    def __init__(self,cw,cwd):
        self.centralwidget = cw
        self.cwd = cwd
        self.pushbutton1()
        self.pushbutton2()
        self.pushbutton3()
        self.pushbutton4()
        self.pushbutton5()
        self.pushbutton6()
        self.pushbutton7()
        # self.pushbutton8()
        self.reconnectServer()
        self.delete_allEntries()
        self.delete_entries()
 
    def pushbutton1(self): #on - off
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(cg.button1_x, cg.button1_y, cg.button1_width, cg.button1_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.push_button), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.button1.setIcon(icon)
        self.button1.setIconSize(QtCore.QSize(cg.button1_width, cg.button1_height))
        self.button1.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button1.setCheckable(False)
        self.button1.setEnabled(True)
        self.button1.setObjectName("push_button")
        # self.button1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
    def pushbutton2(self): # delete last entry
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(cg.button2_x,cg.button2_y, cg.button2_width, cg.button2_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.refresh), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button2.setIcon(icon)
        self.button2.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button2.setIconSize(QtCore.QSize(cg.button2_width, cg.button2_height))
        self.button2.setCheckable(False)
        self.button2.setEnabled(True)
        self.button2.setObjectName("refresh")
        
    def pushbutton3(self): # goto settings tab
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(cg.button3_x,cg.button3_y, cg.button2_width, cg.button2_height))
        # font = QtGui.QFont()
        # font.setFamily("Microsoft Tai Le")
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setUnderline(True)
        # font.setWeight(75)
        # font.setStrikeOut(False)
        # self.button3.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.settings), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button3.setIcon(icon)
        self.button3.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button3.setIconSize(QtCore.QSize(cg.button3_width, cg.button3_height))
        self.button3.setCheckable(False)
        self.button2.setEnabled(True)
        self.button3.setObjectName("settings")
    
    def pushbutton4(self): # go back
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(cg.button4_x,cg.button4_y, cg.button4_width, cg.button4_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.goBack), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button4.setIcon(icon)
        self.button4.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button4.setIconSize(QtCore.QSize(cg.button4_width, cg.button4_height))
        self.button4.setEnabled(False)
        self.button4.setCheckable(False)
        self.button4.hide()
        self.button4.setObjectName("go back")
        

    def pushbutton5(self): # show credits
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(cg.button3_x,cg.button3_y, cg.button2_width, cg.button2_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.credits), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button5.setIcon(icon)
        self.button5.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button5.setIconSize(QtCore.QSize(cg.button5_width, cg.button5_height))
        self.button5.setCheckable(False)
        self.button5.setEnabled(False)
        self.button5.hide()
        self.button5.setObjectName("credits")
        
    def pushbutton6(self): # show server settings
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(cg.button1_x+10,cg.button1_y-50, cg.button6_width, cg.button6_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.server_settings), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button6.setIcon(icon)
        self.button6.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button6.setIconSize(QtCore.QSize(cg.button6_width, cg.button6_height))
        self.button6.setCheckable(False)
        self.button6.setEnabled(False)
        self.button6.hide()
        self.button6.setObjectName("commPorts")
     
    def pushbutton7(self): # show display settings
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(cg.button1_x+10,cg.button1_y+100, cg.button6_width, cg.button6_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.display), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button7.setIcon(icon)
        self.button7.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button7.setIconSize(QtCore.QSize(cg.button6_width, cg.button6_height))
        self.button7.setCheckable(False)
        self.button7.setEnabled(False)
        self.button7.hide()
        self.button7.setObjectName("display") 

    def pushbutton8(self): # change comm port
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(cg.button3_x-5,cg.button3_y-5, cg.button8_width, cg.button8_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.newUsb), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button8.setIcon(icon)
        self.button8.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button8.setIconSize(QtCore.QSize(cg.button8_width, cg.button8_height))
        self.button8.setCheckable(False)
        self.button8.setEnabled(False)
        self.button8.hide()
        self.button8.setObjectName("changeCommPort") 
        
    def reconnectServer(self): # reconnect server
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(cg.button9_x, cg.button9_y, cg.button9_width, cg.button9_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.reconnectServer), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.button9.setIcon(icon)
        self.button9.setIconSize(QtCore.QSize(cg.button9_width, cg.button9_height))
        self.button9.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button9.setCheckable(False)
        self.button9.setEnabled(True)
        self.button9.setObjectName("reconnectServer")
        
    def delete_entries(self): # delete a number of entries
        self.button10 = QtWidgets.QPushButton(self.centralwidget)
        self.button10.setGeometry(QtCore.QRect(cg.button10_x, cg.button10_y, cg.button10_width, cg.button10_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.del_entries), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.button10.setIcon(icon)
        self.button10.setIconSize(QtCore.QSize(cg.button10_width, cg.button10_height))
        self.button10.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button10.setCheckable(False)
        self.button10.setEnabled(False)
        self.button10.hide()
        self.button10.setObjectName("delete_entries")
        
    def delete_allEntries(self): # delete all entries
        self.button11 = QtWidgets.QPushButton(self.centralwidget)
        self.button11.setGeometry(QtCore.QRect(cg.button10_x, cg.button10_y+150, cg.button10_width, cg.button10_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.del_all_entries), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.button11.setIcon(icon)
        self.button11.setIconSize(QtCore.QSize(cg.button10_width, cg.button10_height))
        self.button11.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button11.setCheckable(False)
        self.button11.setEnabled(False)
        self.button11.hide()
        self.button11.setObjectName("delete_all_entries")    
    
        

        