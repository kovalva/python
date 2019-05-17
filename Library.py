"""Document containing Library class description."""
from JsonFile import JsonFile


class Library:
    """Class that implements the functionality of the library,
       allowing you to search, add, remove, take and return books.
    """
    def __init__(self):
        """A constructor that initializes a JsonFile class object,
           thereby generating a JSON file to store library data.
           These data are read from the generated
           JSON file in the self.books variable.
           The list self.book_attributes has a list
           of structure attributes names.
        """
        self.JsonObj = JsonFile("LibraryData.json", "Books.csv")
        self.books = self.JsonObj.read_from_json(self.JsonObj.json_file_path)
        self.book_attributes = ["Title", "Author", "Country", "Language",
                                "Genre", "Pages", "Take_status"]

    def SearchBook(self, search_book):
        """The function that receives data for searching books in a library
           and returns books that satisfy the search terms.

        :param search_book: A set of data in dictionary form
         that is used to search for books.
        :return: List of books corresponding to the received data.
        """
        matching_book = []
        for book in self.books:
            true_flag = True
            for key in search_book.keys():
                if not search_book[key] == '' \
                        and search_book[key] != str(book[key]):
                    true_flag = False
                    break
            if true_flag:
                matching_book.append(book)
        return matching_book

    def AddBook(self, new_book):
        """The function that receives a dictionary with the data
           about the book(-s), checks them for correctness
           and adds it to the library if everything is correct.
           Updates JSON file with library data.

        :param new_book: Dictionary with data about
                         the book(-s) to be added to the library.
        :return: True if book was added and false in another case.
        """
        if self.ValidBook(new_book):
            self.books.append(self.JsonObj.json_structure(new_book))
            self.JsonObj.update_json(self.JsonObj.json_file_path, self.books)
            return True
        else:
            return False

    def DeleteBook(self, delete_book):
        """The function that receives a dictionary with the data
           about the book(-s) and remove it from the library.
           Updates JSON file with library data.

        :param delete_book: Dictionary with data about
                            the book(-s) to be removed from the library.
        :return: True if function works.
        """
        for book in delete_book:
            self.books.remove(book)
        self.JsonObj.update_json(self.JsonObj.json_file_path, self.books)
        return True

    def TakeBook(self, take_book):
        """The function that receives a dictionary with the data
           about the book(-s) and change their Take_status on the 'true'.
           Updates JSON file with library data.

        :param take_book: Dictionary with data about
                          the book(-s) to be taken from the library.
        :return: Nothing.
        """
        for book in take_book:
            book_index = self.books.index(book)
            self.books[book_index]["Take_status"] = "True"
        self.JsonObj.update_json(self.JsonObj.json_file_path, self.books)

    def ReturnBook(self, return_book):
        """The function that receives a dictionary with the data
           about the book(-s) and change their Take_status on the 'false'.
           Updates JSON file with library data.

        :param return_book: Dictionary with data about
                            the book(-s) to be returned from the library.
        :return: Nothing.
        """
        for book in return_book:
            book_index = self.books.index(book)
            self.books[book_index]["Take_status"] = "False"
        self.JsonObj.update_json(self.JsonObj.json_file_path, self.books)

    def PrintBooks(self, books):
        """The function that receives a list of dictionaries
           with book information and prints it.

        :param books: List of dictionaries that contain information
                      about books in corresponding JSON structure
        :return: True if function works.
        """
        for book in books:
            for key in self.book_attributes:
                print("\t\t" + key + ": " + str(book[key]))
            print()
        return True

    def ValidBook(self, book):
        """The function that receives a dictionary
           with the data about the book
           and checks the data for correctness.

        :param book: Dictionary that contain information
                      about books in corresponding JSON structure
        :return: True if data is correct and false in another case.
        """
        for element in book:
            if element == "":
                return False
        try:
            if int(book[5]) <= 0:
                return False
            bool(book[6])
        except ValueError:
            return False

        return True
