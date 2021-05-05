import mysql.connector
from sshtunnel import SSHTunnelForwarder
import time
from datetime import datetime
import socket
import sshtunnel
from config import key, TABLE_NAME
import yaml
from cryptography.fernet import Fernet
import os
from PasswordManager import PasswordManager
import csv

class database:

    def __init__(self, *args):
        self.db_state = 0
        self.mycursor = None
        self.totalIDs = None
        self.internetConnectivity = self.checkInternetSocket()
        try:
            self.serverINFO = PasswordManager(args[0]).retrieveServerCredentials(args[1])
            self.server = args[1]
        except IndexError:
            self.server = 'remote'
            self.serverINFO = PasswordManager(args[0]).retrieveServerCredentials()
        self.connectDB()
        
    # establish connection to database
    def connectDB(self):
        if self.server == 'remote' :
            try:
                self.tunnel = SSHTunnelForwarder((self.serverINFO['SSH_HOST'], int(self.serverINFO['SSH_PORT'])), 
                                            ssh_password=self.serverINFO['SSH_PSWD'], 
                                            ssh_username=self.serverINFO['SSH_USER'], 
                                            remote_bind_address=(self.serverINFO['DB_HOST'], int(self.serverINFO['DB_PORT']))) 
                self.tunnel.start()
                self.myDB = mysql.connector.connect(
                    host=self.serverINFO['DB_HOST'],
                    port=self.tunnel.local_bind_port,
                    user=self.serverINFO['DB_USER'],
                    password=self.serverINFO['DB_PSWD'],
                    database=self.serverINFO['DB_NAME'])
                self.table_name = 'init_devices'
                self.db_state = 1
                self.mycursor = self.myDB.cursor()
                print("Remote server connection established successfully")
            except mysql.connector.errors.InterfaceError:
                self.db_state = 0
                print("Remote server connection failed")

            return self.db_state
        elif self.server == 'local':
            try:
                self.myDB = mysql.connector.connect(
                        host=self.serverINFO['local_DB_HOST'],
                        port=3306,
                        user=self.serverINFO['local_DB_UNAME'],
                        password=self.serverINFO['local_DB_PSWD'],
                        database=self.serverINFO['local_DB_NAME'])
                self.table_name = self.serverINFO['local_DB_TABLE']
                self.db_state = 1
                self.mycursor = self.myDB.cursor()
                print("Local server connection established successfully")
            except mysql.connector.errors.InterfaceError:
                self.db_state = 0
                print("Local server connection failed")
            return self.db_state
    
    # add new entries
    
    def addNew(self, Sim, ID, Password, CreatedOn):
        try:
            self.mycursor.execute(
                "INSERT INTO {}(Sim, ID, Password, CreatedOn) VALUES(%s, %s, %s, %s)".format(self.table_name), ("R"+str(Sim), "I"+str(ID), Password, CreatedOn))
            self.myDB.commit()
            time.sleep(1)
            print("added to database successfully")
            return True
        except mysql.connector.errors.IntegrityError:
            print("Unique value violated")
            return False

    # describe the table

    def describeTable(self):
        if self.db_state == 1:
            self.mycursor.execute("DESCRIBE {}".format(self.table_name))
            for x in self.mycursor:
                print(x)
        else:
            print("Database not connected")

    # terminate connection with database

    def disconnect(self):
        if self.db_state == 1:
            self.myDB.disconnect()
            self.tunnel.close()
            print("server disconnection protocol successful")

    # clear said table

    def clearTable(self):
        self.mycursor.execute("TRUNCATE TABLE {}".format(self.table_name))
        self.myDB.commit()
        print("The table has been cleared")

    # clear n number of entries from said table

    def clearEntries(self, n):
        if self.myDB:
            try:
                for i in range(n):
                    self.mycursor.execute(
                        "DELETE FROM {} ORDER BY CreatedOn DESC LIMIT 1".format(self.table_name))
                self.myDB.commit()
                print(n, "number of entries deletation succcessfull")
            except AttributeError:
                print("Not connected to Database")
                pass
        else:
            print("database didn't respond")

    # get total number of entries/ID
    def getTotalID(self):
        try:
            self.mycursor.execute("SELECT * FROM {} ".format(self.table_name))            
            return len(self.mycursor.fetchall())
        except:
            print("database connection failed")
            return False

    # get last registered ID of current date
    def getLastID(self):
        self.mycursor.execute("SELECT ID FROM {} ORDER BY CreatedOn DESC LIMIT 1".format(self.table_name))
        lastidYMD = self.mycursor.fetchall()[0][0]
        if lastidYMD[-12:-4] != datetime.today().strftime("%Y%m%d"):
            return 0
        else:
            return int(lastidYMD[-4:])

    
    # check if a stable internet connection is available
    def checkInternetSocket(self, host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port))
            print("stable internet connection")
            return True
        except socket.error:
            # print(ex)
            print("unstable internet connection restored")
            return False

    def exportCSV(self):
        self.mycursor.execute("SELECT * FROM {} ORDER BY CreatedOn DESC".format(self.table_name)) 
        with open('exportedFromDB.csv', 'w', newline='') as file:
            wr = csv.writer(file, dialect='excel')
            for i in self.mycursor.fetchall():
                wr.writerow(i)
            return True

    def importCSV(self):
        self.clearTable()
        try:
            n=0
            with open('exportedFromSheet.csv', 'r') as file:
                csv_data = csv.reader(file, delimiter = ',')
                for i in csv_data:
                    if len(i) > 0:
                        if n == 0:
                            n+=1
                        else:
                            len(i)
                            self.mycursor.execute(
                                "INSERT INTO {}(Sim, ID, Password, CreatedOn) VALUES(%s, %s, %s, %s)".format(self.table_name), (i[0],i[1],i[2],i[3]))
                            self.myDB.commit()
                print("added to database successfully")
                self.myDB.commit()
                return True
        except :
            return False
            

if __name__ == "__main__":
    print("IN DATABASE")
    
    # a = database('')
    # a.connectDB()
    # # a.describeTable()
    # # a.exportCSV()
    # # a.importCSV()
    # # a.clearTable()
    # # print(a.getTotalID())
    # print(a.getLastID())
    # a.disconnect()
