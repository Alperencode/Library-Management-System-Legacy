from database.SQLiteDB import SQLiteDataBase

class BookDB(SQLiteDataBase):
    def __init__(self, databaseName):
        super().__init__(databaseName)
        self.CreateBookTable()

    def CreateBookTable(self):
        query = """CREATE TABLE IF NOT EXISTS books (
            isbn INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            publisher TEXT,
            year INTEGER,
            language TEXT
            )"""
        self.ExecuteSQL(query)

    def AddBook(self, book):
        self.AddToTable("books", (book.isbn,
        book.title,
        book.authors[0],
        book.publisher,
        book.year,
        book.language)
        )

    def GetBooks(self):
        return self.GetTable("books")

    def UpdateBook(self, book):
        query = """UPDATE book SET
        title = ?,
        author = ?,
        publisher = ?,
        year = ?,
        language = ?
        WHERE isbn = ?"""
        self.ExecuteSQL(query, (book.title, book.author, book.publisher, book.year, book.language, book.isbn))

    def DeleteBook(self, isbn):
        query = "DELETE FROM book WHERE isbn = ?"
        self.ExecuteSQL(query, (isbn,))

    def SearchByArg(self, arg, value):
        """
        Example query: SELECT * FROM book WHERE (arg) LIKE (value)
        """
        query = "SELECT * FROM book WHERE ? LIKE ?"
        self.cursor.execute(query, (arg, value))
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()