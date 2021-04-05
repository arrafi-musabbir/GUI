


class Extraction:

	def __init__(self):
		pass


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
            # self.totalIDs = self.getTotalID()
        except mysql.connector.Error:
            self.db_state = 0
            print("Server connection failed")
        return self.db_state



if __name__ == "__main__":
	print("here")
