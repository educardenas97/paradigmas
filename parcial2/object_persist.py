from ZODB import FileStore
from ZODB import DB

storage = FileStore.FileStore('myDB.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

