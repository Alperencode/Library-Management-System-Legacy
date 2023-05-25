from methods.methods import cv2, ReadISBN, GetResult, GatherBook
from database.BookDB import BookDB

def main():
    # Creating the database
    db = BookDB("books.db")
    
    # Starting the capture
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)

    # Read the ISBNs
    ReadISBN(cap)

    # Save to database
    if GetResult():
        db.AddBook(GatherBook())

    # Print the database content (Debug)
    for book in db.GetBooks():
        print(book)

if __name__ == "__main__":
    main()