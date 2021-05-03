from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
import transaction


storage = FileStorage('Data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

root['Clientes'] = ['Pepe', 'Juana', 'ange']
transaction.commit()

print(root.items())
connection.close()

