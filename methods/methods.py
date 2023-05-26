from isbnlib import *
import cv2
import numpy as np
from classes.book import Book

# Global variables
book_dictionary = {}

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

        # Returning the barcode data
        return decoded_info[0]

def ReadISBN(cap):
    """
    Read the ISBN from the barcode
    """
    while cv2.waitKey(1) == -1:
        # Read the frame
        success, img = cap.read()
        
        # Flip the image for mirror effect
        img_flip = cv2.flip(img,1)

        # Show the frame
        cv2.imshow('User', img_flip)

        # Detect barcode
        barcode = DetectBarcode(img_flip)
        
        # If barcode is valid
        if barcode:
            # Try to parse the ISBN
            isbn_meta = ParseISBN(barcode)

            # If ISBN is valid
            if isbn_meta:
                return Book(
                    isbn_meta["ISBN-13"],
                    isbn_meta["Title"],
                    isbn_meta["Authors"],
                    isbn_meta["Publisher"],
                    isbn_meta["Year"],
                    isbn_meta["Language"]
                )

                # Writing the title of the book on the frame (Currently corners are not in this scope)
                # cv2.putText(img, isbn_meta["Title"], (int(corners[0][0][0]), int(corners[0][0][1])-5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color=(0, 255, 0), thickness=2)
            else:
                print("Invalid or Unknown ISBN")

        cv2.waitKey(1)
    
    # If the user exits barcode detection
    return False