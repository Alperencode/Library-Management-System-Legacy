from database.SQLiteDB import SQLiteDataBase


# Will be modified
class UserDB(SQLiteDataBase):
    def __init__(self, databaseName):
        super().__init__(databaseName)
        self.CreateUserTable()

    def CreateUserTable(self):
        query = """CREATE TABLE IF NOT EXISTS user (
            email TEXT PRIMARY KEY,
            password TEXT
            )"""
        self.ExecuteSQL(query)

    def AddUser(self, user):
        db_check = self.SearchByArg("email", user.GetEmail())

        if db_check:
            # User already exists (Warning here)
            print("User already exists (DEBUG)")
            return

        self.AddToTable("user", (
            user.GetEmail(),
            user.GetPassword()
        ))

    def UpdateUser(self, user):
        db_check = self.SearchByArg("email", user.GetEmail())

        if db_check:
            self.DeleteUser(user)
            self.AddUser(user)
        else:
            raise ValueError("user not found in database")

    def GetUsers(self):
        return self.GetTable("user")

    def DeleteUser(self, user):
        query = "DELETE FROM user WHERE email = ?"
        self.ExecuteSQL(query, (user.GetEmail()))

    def SearchByArg(self, arg, value):
        """
        Example query: SELECT * FROM user WHERE (arg) LIKE (value)
        """
        query = "SELECT * FROM user WHERE {} LIKE ?".format(arg)
        self.cursor.execute(query, ('%' + str(value) + '%',))
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
