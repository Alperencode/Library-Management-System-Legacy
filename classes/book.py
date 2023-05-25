class Book:
    def __init__(self, isbn=None, title=None, authors=None, publisher=None, year=None, language=None):
        self.__isbn = isbn
        self.__title = title
        self.__authors = authors
        self.__publisher = publisher
        self.__year = year
        self.__language = language

    def GetISBN(self):
        return self.__isbn
    
    def GetTitle(self):
        return self.__title

    def GetAuthor(self):
        return self.__authors[0]
    
    def GetPublisher(self):
        return self.__publisher
    
    def GetYear(self):
        return self.__year
    
    def GetLanguage(self):
        return self.__language

    def GetBookInfo(self):
        return {
            'isbn': self.GetISBN(),
            'title': self.GetTitle(),
            'author': self.GetAuthor(),
            'publisher': self.GetPublisher(),
            'year': self.GetYear(),
            'language': self.GetLanguage()
        }
    
    def GetBookInfoAsTuple(self):
        return (
            self.GetISBN(),
            self.GetTitle(),
            self.GetAuthor(),
            self.GetPublisher(),
            self.GetYear(),
            self.GetLanguage()
        )