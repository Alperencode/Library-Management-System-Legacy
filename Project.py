from methods.ISBNFunctions import cv2, ReadISBN
from database.BookDB import BookDB


def main():
    # Creating the database
    db = BookDB("books.db")

    # Starting the capture
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)

    book = ReadISBN(cap)

    # Save to database
    if book:
        db.AddBook(book)
    else:
        print("Invalid ISBN, no book added to the database")

    # Print the database content (Debug)
    print("\nDatabase content:")
    for book in db.GetBooks():
        print(book)


if __name__ == "__main__":
    main()
