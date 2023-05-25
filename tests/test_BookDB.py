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
        isbn        = 9786053757818,
        title       = 'Fahrenheit 451',
        authors     = ['Ray Bradbury'],
        year        = 2019,
        language    = 'tr'
    )


def test_CreateBookTable():
    db = BookDB(':memory:')
    db.CreateBookTable()
    
    db.cursor.execute("PRAGMA table_info(books)")
    table_info = db.cursor.fetchall()
    
    assert len(table_info) == 6
    assert table_info[0][1] == 'isbn'
    assert table_info[1][1] == 'title'
    assert table_info[2][1] == 'author'
    assert table_info[3][1] == 'publisher'
    assert table_info[4][1] == 'year'
    assert table_info[5][1] == 'language'


def test_AddBook(db, book):
    db.AddBook(book)
    
    db.cursor.execute("SELECT * FROM books")
    table_info = db.cursor.fetchall()

    assert len(table_info) == 2
    assert table_info[1][0] == 9786053757818
    assert table_info[1][1] == 'Fahrenheit 451'
    assert table_info[1][2] == 'Ray Bradbury'
    assert table_info[1][3] == None
    assert table_info[1][4] == 2019
    assert table_info[1][5] == 'tr'


def test_GetBooks(db):
    table_info = db.GetBooks()
    
    assert len(table_info) == 1
    assert table_info[0][0] == 9780131495081
    assert table_info[0][1] == 'Physics For Scientists And Engineers With Modern Physics'
    assert table_info[0][2] == 'Douglas C. Giancoli'
    assert table_info[0][3] == 'Pearson Education'
    assert table_info[0][4] == 2008
    assert table_info[0][5] == 'en'


def test_DeleteBook(db):
    db.DeleteBook(9780131495081)
    
    db.cursor.execute("SELECT * FROM books")
    table_info = db.cursor.fetchall()

    assert len(table_info) == 0
    with pytest.raises(IndexError):
        table_info[0][0]


def test_SearchByArg(db):
    table_info = db.SearchByArg('title', 'Physics')

    assert len(table_info) == 1
    assert table_info[0][0] == 9780131495081
    assert table_info[0][1] == 'Physics For Scientists And Engineers With Modern Physics'
    assert table_info[0][2] == 'Douglas C. Giancoli'
    assert table_info[0][3] == 'Pearson Education'
    assert table_info[0][4] == 2008
    assert table_info[0][5] == 'en'
    