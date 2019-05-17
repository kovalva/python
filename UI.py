"""Document containing UI class description."""
import os
from Library import Library


class UI:
    """The class implements the user interface
       for interacting with the library.
    """
    def __init__(self):
        """A constructor that initializes a Library class object,
           thereby generating a JSON file to store library data
           and tools for interacting with the library.
           Initialize indents in the main menu and the main program switch.
        """
        self.Library = Library()
        self.__menu_indent = " " * 30
        self.__indent = " " * 20
        self.program_switch = {1: self.SearchCase, 2: self.AddCase,
                               3: self.DeleteCase,
                               4: self.ReturnCase, 5: self.TakeCase,
                               6: self.PrintCase}

    def cls(self):
        """The function that clears the console screen.

        :return: Nothing.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def ProgramLoop(self):
        """The main program cycle that allows you to select one of the menu items.

        :return: True if function works correct.
        """
        while True:
            self.MainMenu()
            choice = self.ValidChoice()
            if not choice:
                continue
            elif choice == 7:
                return True
            else:
                self.program_switch[choice]()

    def ValidChoice(self):
        """The function checks the correctness of the input in the main menu.

        :return: True if choice was correct and false in another case.
        """
        try:
            choice = int(input(self.__indent + "Your choice:  "))

            if 1 <= choice <= 7:
                return choice
            else:
                return False
        except ValueError:
            return False

    def MainMenu(self):
        """The function that prints the main menu.

        :return: Nothing.
        """
        self.cls()
        print(self.__menu_indent + "MENU\n",
              self.__indent + "1. Search book.\n",
              self.__indent + "2. Add book.\n",
              self.__indent + "3. Delete book.\n",
              self.__indent + "4. Return book.\n",
              self.__indent + "5. Take book.\n",
              self.__indent + "6. Print library.\n",
              self.__indent + "7. Exit.\n")

    def SearchCase(self):
        """The function that reads data for a book search,
           calls the search function and print result of search.

        :return: True if result is not empty and false in another case.
        """
        self.cls()
        print(self.__menu_indent + "SEARCH BOOK\n")
        search_book = {key: input(key + ": ")
                       for key in self.Library.book_attributes}

        search_result = self.Library.SearchBook(search_book)
        if search_result:
            self.Library.PrintBooks(search_result)
            input("\nSuccess! Press Enter for continue...")
            return True
        else:
            input("\nEmpty search result! Press Enter for continue...")
            return False

    def AddCase(self):
        """The function that reads information about
           the book(-s) user wants to add,
           calls the add function and print result of action.

        :return: True if book was added and false in another case.
        """
        self.cls()
        print(self.__menu_indent + "ADD BOOK\n")
        add_book = [input("Title: "), input("Author: "), input("Country: "),
                    input("Language: "), input("Genre: "), input("Pages: "),
                    input("TakeStatus: ")]

        if self.Library.AddBook(add_book):
            input("\nBook added! Press Enter for continue...")
            return True
        else:
            input("\nError data! Press Enter for continue...")
            return False

    def DeleteCase(self):
        """The function that reads information about
           the book(-s) user wants to remove,
           calls the remove function and print result of action.

        :return: Nothing.
        """
        self.cls()
        print(self.__menu_indent + "DELETE BOOK\n")
        delete_book = {key: input(key + ": ")
                       for key in self.Library.book_attributes}
        delete_result = self.Library.SearchBook(delete_book)

        if self.ValidChange(delete_result):
            self.Library.DeleteBook(delete_result)
            input("\nSuccess delete! Press Enter for continue...")
        else:
            input("\nDeleting aborted! Press Enter for continue...")

    def ValidChange(self, selected_book):
        """The function that receive information about
           the book(-s) user wants to change
           and asks for permission to make changes.

        :return: True if user accepts and false in another case.
        """
        while True:
            self.cls()
            self.Library.PrintBooks(selected_book)
            choice = input("Actions will be performed for these books."
                           " Are you sure? (Y/n)\nYour choose: ")
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                continue

    def ReturnCase(self):
        """The function that reads information about
           the book(-s) user wants to return,
           calls the return function and print result of action.

        :return: rue if user accepts change and false in another case.
        """
        self.cls()
        print(self.__menu_indent + "RETURN BOOK\n")
        return_book = {key: input(key + ": ")
                       for key in self.Library.book_attributes}
        return_result = self.Library.SearchBook(return_book)

        if self.ValidChange(return_result):
            self.Library.ReturnBook(return_result)
            input("\nSuccess! Press Enter for continue...")
            return True
        else:
            input("\nAction aborted! Press Enter for continue...")
            return False

    def TakeCase(self):
        """The function that reads information about
           the book(-s) user wants to take,
           calls the take function and print result of action.

        :return: True if user accepts change and false in another case.
        """
        self.cls()
        print(self.__menu_indent + "TAKE BOOK\n")
        take_book = {key: input(key + ": ")
                     for key in self.Library.book_attributes}
        take_result = self.Library.SearchBook(take_book)

        if self.ValidChange(take_result):
            self.Library.TakeBook(take_result)
            input("\nSuccess! Press Enter for continue...")
            return True
        else:
            input("\nAction aborted! Press Enter for continue...")
            return False

    def PrintCase(self):
        """The function that prints library contents.

        :return: True if function works.
        """
        self.cls()
        self.Library.PrintBooks(self.Library.books)
        input("\nSuccess! Press Enter for continue...")
        return True


if __name__ == "__main__":
    App = UI()
    App.ProgramLoop()
