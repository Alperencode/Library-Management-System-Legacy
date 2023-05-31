import cv2, numpy as np
from isbnlib import is_isbn10, is_isbn13, meta
from classes.book import Book

def ParseISBN(isbn):
    """
    Parses and returns the associated metadata for the provided ISBN if valid.

    Args:
        isbn: The ISBN number to be parsed.

    Returns:
        dict or bool: ISBN metadata if valid, False otherwise.
    """
    if not is_isbn10(isbn) and not is_isbn13(isbn):
        return False
    else:
        return meta(isbn)


def DetectBarcode(img):
    """
    Detects the barcode in the provided image and returns its data if found.

    Args:
        img: The OpenCV video capture representing the image.

    Returns:
        str or bool: Barcode data as a string if valid, False otherwise.
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
    return False


def ReadISBN(cap):
    """
    Reads the ISBN from the barcode and returns the associated book if valid.

    Args:
        cap: The video capture object for reading frames.

    Returns:
        Book or bool:
                The associated book if a valid ISBN is found.
                False if no valid ISBN is detected or the user exits barcode detection.
    """
    INVALID = 0

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
            else:
                INVALID += 1
                cv2.putText(img_flip, "Invalid ISBN", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('User', img_flip)
        else:
            if INVALID >= 5:
                break

            cv2.putText(img_flip, "No barcode detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('User', img_flip)

        # Wait for the user to press a key to exit (Optional)
        cv2.waitKey(1)
    
    # If the user exits barcode detection
    return False