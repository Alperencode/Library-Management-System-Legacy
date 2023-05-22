import methods
from methods import cv2
from database.SQLiteDB import SQLiteDataBase

def main():
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)

    while cv2.waitKey(1) == -1:
        # Read the frame
        success, img = cap.read()
        
        # Flip the image for mirror effect
        img_flip = cv2.flip(img,1)

        # Detect faces
        methods.DetectFaces(img_flip)

        # Detect barcode
        methods.DetectBarcode(img_flip)

        # Show the frame
        cv2.imshow('User', img_flip)
        
        cv2.waitKey(1)

    # Output the result
    methods.OutputTXT()

if __name__ == "__main__":
    # Example Database usage
    db = SQLiteDataBase(':memory:')

    # Creating a table
    create_table_query = "CREATE TABLE IF NOT EXISTS my_table (id INTEGER, name TEXT, age INTEGER)"
    db.ExecuteSQL(create_table_query)

    # Inserting data into the table
    db.AddToTable("my_table", (3, "Jack", 20))
    db.AddToTable("my_table", (4, "John", 21))

    # Selecting data from the table
    print(db.GetTable("my_table"))

    # main()