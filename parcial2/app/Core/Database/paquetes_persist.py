from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
import transaction


storage = FileStorage('Data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()


def insert(paquete):
    root['Paquete'] = paquete
    transaction.commit()
    connection.close()

def find(object_name):
    return root[object_name]