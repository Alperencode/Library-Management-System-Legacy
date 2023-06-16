from database.SQLiteDB import SQLiteDataBase


# Will be modified
class UserDB(SQLiteDataBase):
    def __init__(self, databaseName):
        super().__init__(databaseName)
        self.CreateUserTable()

    def CreateUserTable(self):
        pass

    def UpdateUser(self, user):
        pass

    def AddBUser(self, user):
        pass

    def GetUsers(self):
        pass

    def DeleteUser(self, id):
        pass

    def SearchByArg(self, arg, value):
        """
        Example query: SELECT * FROM user WHERE (arg) LIKE (value)
        """
        query = "SELECT * FROM user WHERE {} LIKE ?".format(arg)
        self.cursor.execute(query, ('%' + str(value) + '%',))
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
