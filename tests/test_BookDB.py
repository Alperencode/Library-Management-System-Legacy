from classes.book import Book
from database.BookDB import BookDB
import pytest

@pytest.fixture
def db():
    db = BookDB(':memory:')
    db.ExecuteSQL(
        "INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", 
        (9780131495081, 'Physics For Scientists And Engineers With Modern Physics', 'Douglas C. Giancoli', 'Pearson Education', 2008, 'en')
    )
    return db


@pytest.fixture
def book():
    return Book(
        isbn        = 9780131495081,
        title       = 'Physics For Scientists And Engineers With Modern Physics',
        authors     = ['Douglas C. Giancoli'],
        publisher   = 'Pearson Education',
        year        = 2008,
        language    = 'en'
    )


@pytest.fixture
def new_book():
    return Book(
        isbn        = 9786053757818,
        title       = 'Fahrenheit 451',
        authors     = ['Ray Bradbury'],
        year        = 2019,
        language    = 'tr'
    )


def test_CreateBookTable(book):
    db = BookDB(':memory:')
    db.CreateBookTable()
    
    db.cursor.execute("PRAGMA table_info(books)")
    table_info = db.cursor.fetchall()
    
    assert len(table_info) == 6
    for index, item in enumerate(book.GetBookInfo().keys()):
        assert table_info[index][1] == item

def test_AddBook(db, new_book, book):
    db.AddBook(new_book)
    
    db.cursor.execute("SELECT * FROM books")
    table_info = db.cursor.fetchall()

    assert len(table_info) == 2
    for i in range(6):
        assert table_info[1][i] == new_book.GetBookInfoAsTuple()[i]

    db.AddBook(book)
    assert len(table_info) == 2

def test_UpdateBook(db, new_book, book):
    db.UpdateBook(book)
    
    db.cursor.execute("SELECT * FROM books")
    table_info = db.cursor.fetchall()

    assert len(table_info) == 1
    for i in range(6):
        assert table_info[0][i] == book.GetBookInfoAsTuple()[i]

    with pytest.raises(ValueError):
        db.UpdateBook(new_book)

def test_GetBooks(db, book):
    table_info = db.GetBooks()
    
    assert len(table_info) == 1
    for i in range(6):
        assert table_info[0][i] == book.GetBookInfoAsTuple()[i]

def test_DeleteBook(db, book):
    db.DeleteBook(book.GetISBN())
    
    db.cursor.execute("SELECT * FROM books")
    table_info = db.cursor.fetchall()

    assert len(table_info) == 0
    with pytest.raises(IndexError):
        table_info[0][0]

def test_SearchByArg(db, book):
    table_info = db.SearchByArg('title', 'Physics')

    assert len(table_info) == 1
    for i in range(6):
        assert table_info[0][i] == book.GetBookInfoAsTuple()[i]