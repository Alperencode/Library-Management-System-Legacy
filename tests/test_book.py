from classes.book import Book
import pytest

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

def test_GetISBN(book):
    assert book.GetISBN() == 9780131495081
    assert book.GetISBN() != str(9780131495081)
    with pytest.raises(AttributeError):
        book.__isbn
    
def test_GetTitle(book):
    assert book.GetTitle() == 'Physics For Scientists And Engineers With Modern Physics'
    with pytest.raises(AttributeError):
        book.__title

def test_GetAuthor(book):
    assert book.GetAuthor() == 'Douglas C. Giancoli'
    with pytest.raises(AttributeError):
        book.__authors

def test_GetPublisher(book):
    assert book.GetPublisher() == 'Pearson Education'
    with pytest.raises(AttributeError):
        book.__publisher

def test_GetYear(book):
    assert book.GetYear() == 2008
    with pytest.raises(AttributeError):
        book.__year

def test_GetLanguage(book):
    assert book.GetLanguage() == 'en'
    with pytest.raises(AttributeError):
        book.__language