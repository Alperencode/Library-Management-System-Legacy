# Library Book Matching System

## Overview

This project was developed for the ["Technology For Humanity Competition"](https://www.teknofest.org/en/competitions/competition/51) under the "Social Innovation" subcategory at TeknoFest. The aim of the project was to create a library book matching system that would match books' ISBN code and people's face, thus ensuring a more efficient and secure library experience.

The system consists of two main components: an ISBN book matching system and a face detection system. The ISBN book matching system can read any barcode and find the book via its ISBN code, displaying information such as the book's name, author, and more. The face detection system is able to detect faces, but does not yet match or recognize any individuals.

## Usage

To use the system, you will need to install the necessary dependencies and run the code. The system requires Python 3.8 or higher, as well as the dependencies listed in the requirements.txt file. You can install these dependencies using pip by running the following command:

```bash
pip install -r requirements.txt
```

Once you have installed the dependencies, you can run the code using the following command:

```bash
cd Project
python Project.py
```

This will launch the system, which will prompt you to scan a book's ISBN code or detect a face. Follow the instructions provided by the system to use its various features.

## Future Work

**Although this project was not completed** due to its **elimination from the competition**, there is still room for further development. Some ideas for future work include:

- Implementing a face recognition system to match individuals with their library accounts
- Integrating the system with existing library management software to improve the borrowing and return process
- Adding more features to the system, such as recommendations based on a user's borrowing history