from oauth2client.service_account import ServiceAccountCredentials
import os
import gspread
from google.auth.exceptions import TransportError
import csv
from datetime import datetime

class spreadSheet:

    def __init__(self):
        try:
            os.makedirs('CSVs')
        except FileExistsError:
            pass
        self.csv_path = os.path.join(os.getcwd(),'CSVs')
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
            with open(os.path.join(self.csv_path,'exportedFromSheet_{}.csv'.format(datetime.today().strftime('%d %b %Y'))), 'w', newline='') as file:
                wr = csv.writer(file, dialect='excel')
                wr.writerows(s)  
                return True
        except :
            return False      

    def importCSV(self):
        try:
            content = open(os.path.join(self.csv_path,'exportedFromDB_{}.csv'.format(datetime.today().strftime('%d %b %Y'))), 'r').read()
            self.client.import_csv(self.sheet.id, content)
            return True
        except:
            return False

if __name__ == "__main__":
    a = spreadSheet()
    # print(a.importCSV())
    a.exportCSV()
    pass
