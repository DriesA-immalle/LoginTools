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

    def clearTable(self, table):
        self.cursor.execute('DELETE FROM ' + table)
        self.db.commit()

    def clearWithCondition(self, table, column, condition):
        self.cursor.execute('DELETE FROM ' + table + ' WHERE ' + column + '="' + condition + '"')
        self.db.commit()

    def totalRecords(self, table):
        self.cursor.execute('SELECT * FROM ' + table)
        records = self.cursor.fetchall()
        return len(records)

    def totalRecordsWithCondition(self, table, column, condition):
        self.cursor.execute('SELECT * FROM ' + table + ' WHERE ' + column + '="' + condition + '"')
        records = self.cursor.fetchall()
        return len(records)

if __name__ == "__main__":
    logintools = LoginTools('TestDB')