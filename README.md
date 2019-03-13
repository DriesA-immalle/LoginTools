# LoginTools
Python Library with various methods to assist with login


***Warning Do not use non-verified user input in this library! Various methods are not SQL-injection proof!***


## Tree for this example
```
- PythonLogin
| main.py
| TestDB.sqlite3
```
## Constructor
While calling the constructor, pass the name of your database as a string.
### main.py
```
from LoginTools import *

if __name__ == '__main__':
  logintools = LoginTools('TestDB.sqlite3')
```

## hashInput(inputString)
This method returns the sha256 hash of a given string
### main.py
```
from LoginTools import *

if __name__ == '__main__':
  logintools = LoginTools('TestDB.sqlite3')
  hashedString = logintools.hashInput('this is a test string')
  print(hashedString)
```
### Result
```
f6774519d1c7a3389ef327e9c04766b999db8cdfb85d1346c471ee86d65885bc
```

## checkSQLInjection(inputString)
Returns true or false depending if there is a chance of an SQL query in the given string.
### main.py
```
from LoginTools import *

if __name__ == '__main__':
  logintools = LoginTools('TestDB.sqlite3')
  containsSQL = logintools.checkSQLInjection('ThisCouldBeSQLBecauseItContainsAsemicolon;')
  print(containsSQL)
```
### Result
```
True
```

## checkIgnored()
Run this method right after executing a 'Insert ignore' query. It will return true if the query was ignored due to duplicate data.
### main.py
```
from LoginTools import *
from sqlite3 import connect, Cursor

if __name__ == '__main__':
  logintools = LoginTools('TestDB.sqlite3')
  db = connect('TestDB.sqlite3)
  cursor = db.Cursor()
  
  #For this example column1 is set to UNIQUE and one of the records already contains 'value1'
  logintools.cursor.execute('INSERT OR IGNORE INTO table(column1, column2) VALUES('value1', 'value2')
  db.commit()
  
  ignored = logintools.checkIgnored()
  print(ignored)
```
### Result
```
True
```
