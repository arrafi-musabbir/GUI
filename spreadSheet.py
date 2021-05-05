from oauth2client.service_account import ServiceAccountCredentials
import os
import gspread
from google.auth.exceptions import TransportError
import csv

class spreadSheet:

    def __init__(self):
        self.connectSheet()

    def connectSheet(self):
        try:
            scope = ['https://www.googleapis.com/auth/spreadsheets',
                    'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                filename=os.path.join(os.getcwd(), "creds.json"), scopes=scope)
            self.client = gspread.authorize(creds)
            self.sheet = self.client.open("device-id-and-pswd")
            print("connection extablished with google spreadsheet")
            return True
        except TransportError:
            print("couldn't establish a connection with google spreadsheet\nCheck your internet connections")
            return False
        
    def exportCSV(self):
        try:
            sheet = self.sheet.sheet1
            s = sheet.get_all_values()
            # print(s)
            with open('exportedFromSheet.csv', 'w', newline='') as file:
                wr = csv.writer(file, dialect='excel')
                wr.writerows(s)  
                return True
        except :
            return False      

    def importCSV(self):
        try:
            content = open('exportedFromDB.csv', 'r').read()
            self.client.import_csv(self.sheet.id, content)
            return True
        except:
            return False

if __name__ == "__main__":
    # a = spreadSheet()
    # # a.importCSV()
    # a.exportCSV()
    pass
