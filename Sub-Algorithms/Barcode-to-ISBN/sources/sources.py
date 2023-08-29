from isbnlib import meta, is_isbn10, is_isbn13

# Global variables
result_dictionary = {}
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
    if isbn_meta["Title"] != last_book:
        print("Title:", isbn_meta["Title"])
        last_book = isbn_meta["Title"]
    # print("Kitap:", isbn_meta["Title"])
    for key, value in isbn_meta.items():
        result_dictionary[key] = value


def OutputTXT():
    """
    Output the result dictionary to a txt file
    """
    with open('output.txt', 'w', encoding='utf-8') as f:
        for key, value in result_dictionary.items():
            if type(result_dictionary[key]) is list:
                f.write(f"{key}: ")
                for item in result_dictionary[key]:
                    if item != result_dictionary[key][-1]:
                        f.write(f"{item}, ")
                    else:
                        f.write(f"{item}")
                f.write("\n")
            else:
                f.write(f"{key}: {value}\n")


def GetResult():
    """ Getter for the result dictionary """
    return result_dictionary
