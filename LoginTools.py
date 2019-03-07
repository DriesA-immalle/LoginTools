from sqlite3 import connect, Cursor
import hashlib

class LoginTools():
    def __init__(self, dbName):
        self.db = connect(dbName)
        self.cursor = self.db.cursor()
        self.hash = hashlib.sha256()

    def hashInput(self, inputString):
        self.hash.update(inputString.encode('utf-8'))
        return self.hash.hexdigest()

    def checkSQLInjection(self, inputString):
        if ' ' in inputString or ';' in inputString:
            return True
        else:
            return False

    def checkIgnored(self):
        if self.cursor.lastrowid == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    logintools = LoginTools('TestDB')