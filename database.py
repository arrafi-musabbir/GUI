import mysql.connector
import time
from datetime import datetime 

class database:

    def __init__(self):
        self.db_state = 0
        self.mycursor = None
        self.totalIDs = None
        # self.connectDB()
        

    def connectDB(self):
        try:
            self.myDB = mysql.connector.connect(
                host="localhost",
                user="root",
                password="#456",
                database="deviceinfo")
            self.db_state = 1
            self.mycursor = self.myDB.cursor()
            print("Server connection established successfully")
            self.mycursor.execute("ALTER TABLE deviceid AUTO_INCREMENT=1;")
            self.totalIDs = self.getTotalID()
        except mysql.connector.Error:
            self.db_state = 0
            print("Server connection failed")

        return self.db_state

    def addNew(self, ID, sim, PSWD, DateTime):
        try:
            self.mycursor.execute(
                "INSERT INTO deviceid(ID, Sim, password, CreatedOn) VALUES(%s, %s, %s, %s)", (ID, sim, PSWD, DateTime))
            self.myDB.commit()
            time.sleep(1)
            print("added successfully")
            return True
        except mysql.connector.errors.IntegrityError:
            return False

    def describeTable(self):
        self.mycursor.execute("DESCRIBE deviceid")
        for x in self.mycursor:
            print(x)

    def disconnect(self):
        self.myDB.disconnect()

    def clearTable(self):
        self.mycursor.execute("TRUNCATE TABLE deviceid")
        self.myDB.commit()
        print("The table has been cleared")

    def clearEntries(self, n):
        if self.myDB:
            try:
                for i in range(n):
                    self.mycursor.execute(
                        "DELETE FROM deviceid ORDER BY CreatedOn DESC LIMIT 1")
                self.myDB.commit()
                print(n,"number of entries deletation succcessfull")
            except AttributeError:
                print("Not connected to Database")
                pass
        else:
            print("helele")

    def getTotalID(self):
        try:
            self.mycursor.execute(
                "SELECT Serial FROM deviceid ORDER BY CreatedOn DESC LIMIT 1")
            for i in self.mycursor:
                return i[0]
        except:
            print("database connection failed")

if __name__ == "__main__":
    print("IN DATABASE")
    a = database()
    # a.connectDB()
    # a.describeTable()
    # print(a.db_state)
    # a.addNew( "33" , "18722", "tihan", datetime.now())
    # time.sleep(1)
    # print(a.getTotalID())
    # a.clearTable()
    # a.clearEntries(1)
    # a.disconnect()
