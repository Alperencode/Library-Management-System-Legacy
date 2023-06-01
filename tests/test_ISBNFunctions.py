import pytest
import cv2
from methods.ISBNFunctions import ParseISBN, DetectBarcode, ReadISBN


def test_ParseISBN():
    assert ParseISBN("9780131495081") == {
        "ISBN-13": "9780131495081",
        "Title": "Physics For Scientists And Engineers With Modern Physics",
        "Authors": ["Douglas C. Giancoli"],
        "Publisher": "Pearson Education",
        "Year": '2008',
        "Language": "en"
    }

    assert ParseISBN("978-1-56619-909-3") == False