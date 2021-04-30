from cryptography.fernet import Fernet
import random
from datetime import datetime
import os
from config import key

class genID:

    def __init__(self):
        self.today = datetime.today().strftime("%Y%m%d")
        self.keysList = list()
        self.key = None
        self.id = None
        self.retrieveKeys()

    def newID(self, newSerial):
        self.key = self.randomKey()
        # print(self.key[0],":",self.key[1:])
        self.encryption_type = Fernet(self.key[1:].encode())
        # print("Total number of IDs stored already:>> ", newSerial)
        pswd = str(random.randint(1000, 9999))
        # print("random pswd", pswd)
        self.en_pswd = self.key[0] + self.enPswd(pswd).decode()
        # print(len(self.en_pswd))
        self.id = pswd + "1103" + self.today + '0000'
        self.id = str(int(self.id) + newSerial)
        # print("New generated ID:>> ", self.id[0:4] + " " + self.id[4:8] + " "
        #       + self.id[8:12] + " " + self.id[12:14] + " " + self.id[14:16] + " " + self.id[16:])
        return self.id, self.en_pswd

    def randomKey(self):
        return random.choice(self.keysList)

    def enPswd(self, pswd):
        return self.encryption_type.encrypt(pswd.encode())

    def dePswd(self, en_pswd):

        return str(self.encryption_type.decrypt(en_pswd.encode()))

    def retrieveKeys(self):

        with open(os.path.join(os.getcwd(), "keys.key"), "r") as k:
            for i in k:
                key = i.strip()
                self.keysList.append(key)
        print("Keys retrieved")
        # print(self.keysList)


if __name__ == "__main__":
    import yaml
    s = dict()
    print(key)
    a = Fernet(key)
    with open('creds.yml', 'r') as f:
        y = yaml.safe_load(f)
        for i in y:
            # print(y[i])
            try:
                s[i] = a.decrypt(y[i].encode()).decode()
                # print(i)
            except cryptography.fernet.InvalidToken:
                pass
    # print(type(s['DB_HOST']))
    # print(s)
    for i in s:
            # print(i)
            s[i] = a.encrypt(str(s[i]).encode()).decode()
            print(s[i])
    # with open('creds.yml', 'w') as f:
    #     for i in s:
    #         print(i)
    #         s[i] = a.encrypt(str(s[i]).encode()).decode()
    #         print(s[i])
    #     s['key'] = key.decode()
    #     yaml.dump(s, f)
        
        
    # print(a.newID(1)[0])
