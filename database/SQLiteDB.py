import sqlite3, re
from classes.book import Book

class SQLiteDataBase:
    def __init__(self, databaseName):
        self.databaseName = databaseName
        self.conn = sqlite3.connect(self.databaseName)
        self.cursor = self.conn.cursor()

    @staticmethod
    def SanitizeName(tableName):
        # Define the allowed characters for the table name
        allowedCharacters = r'[a-zA-Z0-9_]+'
        
        # Remove any potentially harmful characters from the table name
        sanitizedTableName = re.sub(r'[^a-zA-Z0-9_]', '', tableName)
        
        # Validate the table name
        if re.fullmatch(allowedCharacters, sanitizedTableName):
            return sanitizedTableName
        else:
            raise ValueError("Invalid table name.")
    
    def ExecuteSQL(self, query, *parameters):
        if parameters:
            self.cursor.executemany(query, parameters)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def AddToTable(self, tableName, parameters=None):
        if not parameters:
            parameters = ()
        tableName = SQLiteDataBase.SanitizeName(tableName)
        query = "INSERT INTO {} VALUES ({})".format(
            tableName, ", ".join("?" * len(parameters))
        )
        self.cursor.execute(query, parameters)
        self.conn.commit()

    def GetTable(self, tableName):
        tableName = SQLiteDataBase.SanitizeName(tableName)
        query = "SELECT * FROM {}".format(tableName)
        self.cursor.execute(query)
        return self.cursor.fetchall()