import mysql.connector
from sshtunnel import SSHTunnelForwarder
import time
from datetime import datetime
import socket
from random import randint
import sshtunnel
from config import key, TABLE_NAME
import yaml
from cryptography.fernet import Fernet

class database:

    def __init__(self, server):
        self.db_state = 0
        self.mycursor = None
        self.totalIDs = None
        self.internetConnectivity = self.checkInternetSocket()
        self.connectDB(server)

    # establish connection to database
    def connectDB(self, server):
        self.serverINFO = dict()
        def decryptServerINFO():
            with open('creds.yml', 'r') as file:
                serverINFO = yaml.safe_load(file)
                a = Fernet(key.encode())
                for i in serverINFO:
                    self.serverINFO[i] = a.decrypt(serverINFO[i].encode()).decode()
        if server == 'remote':
            try:
                decryptServerINFO()
                serverINFO = self.serverINFO
                self.tunnel = SSHTunnelForwarder((serverINFO['SSH_HOST'], int(serverINFO['SSH_PORT'])), 
                                            ssh_password=serverINFO['SSH_PSWD'], 
                                            ssh_username=serverINFO['SSH_UNAME'], 
                                            remote_bind_address=(serverINFO['DB_HOST'], int(serverINFO['DB_PORT']))) 
                self.tunnel.start()
                self.myDB = mysql.connector.connect(
                    host=serverINFO['DB_HOST'],
                    port=self.tunnel.local_bind_port,
                    user=serverINFO['DB_UNAME'],
                    password=serverINFO['DB_PSWD'],
                    database=serverINFO['DB_NAME'])
                self.table_name = TABLE_NAME
                self.db_state = 1
                self.mycursor = self.myDB.cursor()
                print("Server connection established successfully")
            except mysql.connector.errors.InterfaceError:
                self.db_state = 0
                print("Server connection failed")

            return self.db_state
        else:
            try:
                self.myDB = mysql.connector.connect(
                        host=serverINFO['local_DB_HOST'],
                        port=3306,
                        user=serverINFO['local_DB_UNAME'],
                        password=serverINFO['local_DB_PSWD'],
                        database=serverINFO['local_DB_NAME'])
                self.table_name = 'deviceid'
                self.db_state = 1
                self.mycursor = self.myDB.cursor()
                print("Server connection established successfully")
            except mysql.connector.errors.InterfaceError:
                self.db_state = 0
                print("Server connection failed")
            return self.db_state
    
    
        
        
    # add new entries
    
    def addNew(self, Sim, ID, Password, CreatedOn):
        try:
            self.mycursor.execute(
                "INSERT INTO {}(Sim, ID, Password, CreatedOn) VALUES(%s, %s, %s, %s)".format(self.table_name), (Sim, ID, Password, CreatedOn))
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
            # self.mycursor.execute(
            #     "SELECT Serial FROM deviceid ORDER BY CreatedOn DESC LIMIT 1")
            self.mycursor.execute("SELECT * FROM {}".format(self.table_name))
            num_rows = self.mycursor.fetchall()
            return len(num_rows)

        except:
            print("database connection failed")
            return False

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


if __name__ == "__main__":
    print("IN DATABASE")
    a = database('remote')
    # a.connectDB()
    a.describeTable()
    # a.clearTable()
    a.disconnect()
