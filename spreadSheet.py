from oauth2client.service_account import ServiceAccountCredentials
import os
import gspread

class spreadSheet:
    
    def __init__(self):
        self.connectSheet()
        
    def connectSheet(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
                filename=os.path.join(os.getcwd(), "creds.json"), scopes=scope)
        client = gspread.authorize(creds)
        self.sheet = client.open("DEVICE ID").sheet1
        print("connection extablished")
        return None    

    def del_lastID(self):
        self.get_totalIDs()
        print("Currently total id stored:", self.total_ids)
        if self.total_ids != 0:
            self.sheet.delete_rows(self.total_ids + 1)
            self.sheet.update_acell("A2", self.total_ids - 1)
            print("New total id stored after one deletion: ", self.get_totalIDs())
        else:
            print("No id stored")
        return None

    def get_a_value(self, s):

        if s[0] == "C":
            return self.dePswd(self.sheet.acell(s).value)
        else:
            return self.sheet.acell(s).value

    def saveToSheet(self):

        if self.total_ids == 0:
            self.sheet.update_acell(
                "B" + str(self.total_ids + 2), str(self.id[4:]))
            self.sheet.update_acell(
                "C" + str(self.total_ids + 2), self.en_pswd.decode())
            self.sheet.update_acell("A2", self.total_ids + 1)
            self.total_ids = self.total_ids + 1

        else:
            print("new id added")
            self.sheet.update_acell(
                "B" + str(self.total_ids + 2), str(self.id[4:]))
            # print(type(self.en_pswd))
            self.sheet.update_acell(
                "C" + str(self.total_ids + 2), self.en_pswd.decode())
            self.sheet.update_acell("A2", self.total_ids + 1)
            self.total_ids = self.total_ids + 1

if __name__ == "__main__":
    a = spreadSheet()