from methods.methods import cv2, ReadISBN, OutputTXT, GetResult, GatherBook
from database.BookDB import BookDB

def main():
    db = BookDB("books.db")
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)

    ReadISBN(cap)

    # Output the result
    # methods.OutputTXT()

    # Save to database
    if GetResult():
        db.AddBook(GatherBook())

    for book in db.GetBooks():
        print(book)

if __name__ == "__main__":
    main()