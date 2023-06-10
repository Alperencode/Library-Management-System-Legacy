import sqlite3
import re


class SQLiteDataBase:
    def __init__(self, databaseName):
        self.databaseName = databaseName
        self.conn = sqlite3.connect(self.databaseName)
        self.cursor = self.conn.cursor()

    @staticmethod
    def SanitizeName(database_name):
        # Remove invalid characters from the database name
        sanitized_name = re.sub(
            r'[!@#$%^&*()+={}\[\]|\\\"\'<>.,/?~\n\r\t]',
            '',
            database_name)

        sanitized_name = sanitized_name.strip()

        # Empty string check
        if not sanitized_name:
            raise ValueError("DB name contains only invalid characters.")

        # Reserved keyword check
        reserved_keywords = [
            "SELECT", "FROM", "WHERE", "INSERT", "UPDATE", "DELETE",
        ]
        if sanitized_name.upper() in ' '.join(reserved_keywords).upper():
            raise ValueError("DB name contains reserved keywords.")

        # Starts with a digit check
        if sanitized_name[0].isdigit():
            raise ValueError("DB name cannot start with a digit.")

        # Valid name
        return sanitized_name

    def ExecuteSQL(self, query, *parameters):
        if parameters:
            self.cursor.executemany(query, parameters)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def AddToTable(self, tableName, parameters=None):
        if (not parameters) or (not tableName):
            return
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
