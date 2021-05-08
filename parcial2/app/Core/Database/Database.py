from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
import transaction


class Database():
    def __init__(self, path='app/Core/Database/Data.fs'):
        self.storage = FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def insert(self, object, object_name):
        self.root[object_name] = object
        transaction.commit()
        self.connection.close()

    def find(self, object_name):
        return self.root[object_name]
