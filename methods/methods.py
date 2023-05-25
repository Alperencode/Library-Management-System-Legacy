from isbnlib import *
import cv2
import numpy as np
from classes.book import Book

# Global variables
book_dictionary = {}
last_book = ""

def ParseISBN(isbn):
    """
    Parsing the ISBN number
    If ISBN is valid, return the metadata
    Else return False
    """
    if not is_isbn10(isbn) and not is_isbn13(isbn):
        return False
    else:
        return meta(isbn)

def ParseMeta(isbn_meta):
    """
    Parsing the metadata from the ISBN
    If data is valid, update the result dictionary
    """
    global last_book
    for key, value in isbn_meta.items():
        book_dictionary[key] = value

    if isbn_meta["Title"] != last_book:
        for key, value in book_dictionary.items():
            print(f"{key}: {value}")
        last_book = isbn_meta["Title"]

def DetectBarcode(img):
    """
    Detect barcode in the frame
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = cv2.barcode_BarcodeDetector()

    # Detecting the barcode
    # Respectively: validation, barcode data, decode type, points of the barcode
    valid, decoded_info, decoded_type, corners = detector.detectAndDecode(gray)

    # If barcode is valid
    if valid:
        # Drawing the polygon around the barcode
        int_corners = np.array(corners, dtype=np.int32)
        cv2.polylines(img, [int_corners], True, (0, 255, 0), 5)

        # Parsing ISBN data
        isbn_meta = ParseISBN(decoded_info[0])

        # If ISBN is valid
        if isbn_meta:
            # Parsing the metadata
            ParseMeta(isbn_meta)

            # Writing the title of the book
            cv2.putText(img, isbn_meta["Title"], (int(corners[0][0][0]), int(corners[0][0][1])-5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color=(0, 255, 0), thickness=2)
        else:
            print("Invalid or Unknown ISBN")

def ReadISBN(cap):
    """
    Read the ISBN from the barcode
    """
    while cv2.waitKey(1) == -1:
        # Read the frame
        success, img = cap.read()
        
        # Flip the image for mirror effect
        img_flip = cv2.flip(img,1)

        # Detect faces
        # DetectFaces(img_flip)

        # Detect barcode
        DetectBarcode(img_flip)

        # Show the frame
        cv2.imshow('User', img_flip)
        
        # If any result is found, break the loop
        if GetResult():
            break

        cv2.waitKey(1)

def GetResult():
    """ 
    Getter for the book dictionary 
    """
    return book_dictionary

def GatherBook():
    book = Book(
        book_dictionary["ISBN-13"],
        book_dictionary["Title"],
        book_dictionary["Authors"],
        book_dictionary["Publisher"],
        book_dictionary["Year"],
        book_dictionary["Language"])
    return book