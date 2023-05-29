# Library Book Matching System

## Overview

This project is a library book matching system developed for a personal project. The aim of the project is to create an efficient and secure library experience by matching books' ISBN codes using barcode recognition and a **SQLite** database.

The system consists of a barcode recognition system that can read ISBN codes and retrieve information about the corresponding book, such as its title and author.

## Usage

To get started with the Library Book Matching System, follow these steps using your prompt or terminal:

1. Clone the repository:
    - Clone the project repository
        ```bash
        git clone https://github.com/Alperencode/Library-Management-System.git
        ```
    - Navigate to project directory
        ```bash
        cd Library-Management-System
        ```

2. Install Dependencies:
   - Ensure you have Python 3.8 or a higher version installed on your system.
   - Install the necessary dependencies by running the following command:
     ```bash
     pip install -r requirements.txt
     ```

3. Launch the System:
   - Execute the system by entering the following command:
     ```bash
     python Project.py
     ```

4. Scan ISBN Codes:
   - Once the system is running, it will prompt you to scan a book's ISBN code using a barcode scanner.
   - Follow the instructions provided by the system to retrieve detailed information about the book, including its title and author.

## Sample Image

<img src="images/Project-Sample.png">

<br>

## Future Work

- **Graphical User Interface (GUI):** 
  - Develop a user-friendly GUI for easy navigation and book management.
<br>

- **User Authentication and Account Management:** 
  - Implement secure user login and account management functionality.
<br>


- **Barcode Detection for Book Addition:**
  - Allow users to add books to their accounts using barcode detection.
<br>

- **Automated Book Suggestions:**
  - Provide personalized book recommendations based on user preferences.
<br>

- **Inventory Management and Notifications:**
  - Create an automated system for book inventory management and user notifications.
<br>

- **Integration with Online Libraries:**
  - Explore integrating the system with online libraries or book databases.
<br>

*By implementing these enhancements, the Library Book Matching System can become a comprehensive and user-friendly platform, offering seamless book management and a delightful library experience.*

<br>

## Directory Structure

```
Library-Book-Matching-System
├── .github
│   └── workflows
│       └── python-app.yml
├── classes
│   └── book.py
├── database
│   ├── __init__.py
│   ├── BookDB.py
│   └── SQLiteDB.py
├── images
│   └── Project-Sample.png
├── methods
│   └── methods.py
├── Sub-Algorithms
│   ├── Barcode-Detection
│   ├── Barcode-to-ISBN
│   ├── Face-Detection
│   └── Yolo
│       ├── Yolo-320
│       └── Yolo-Tiny
├── tests
│   ├── __init__.py
│   └── test_SQLiteDB.py
├── .gitignore
├── __init__.py
├── books.db
├── Project.py
├── README.md
└── requirements.txt
```