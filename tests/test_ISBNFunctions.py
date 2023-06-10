import pytest
from methods.ISBNFunctions import ParseISBN


@pytest.fixture
def meta_data():
    return {
        "ISBN-13": "9780131495081",
        "Title": "Physics For Scientists And Engineers With Modern Physics",
        "Authors": ["Douglas C. Giancoli"],
        "Publisher": "Pearson Education",
        "Year": '2008',
        "Language": "en"
    }


def test_ParseISBN(meta_data):
    assert ParseISBN("9780131495081") == meta_data
    assert ParseISBN(9780131495081) == meta_data
    assert ParseISBN("978-1-56619-909-3") is False


def test_DetectBarcode():
    # DetectBarcode() takes videoCapture as an argument
    # Skipping this test
    pass


def test_ReadISBN():
    # ReadISBN() takes videoCapture as an argument
    # Skipping this test
    pass
