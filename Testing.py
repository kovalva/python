import unittest
from UI import UI
from JsonFile import JsonFile

TestProgram = UI()
TestJson = JsonFile("LibraryData.json", "Books.csv")

str_book_false = ["", "Sometxt", "Sometxt", "Sometxt", "Sometxt",
                  "Sometxt", "true"]
str_book_true = ["Sometxt", "Sometxt", "Sometxt", "Sometxt",
                 "Sometxt", "5", "true"]
book = {
    'Title': "Sometxt",
    'Author': "Sometxt",
    'Country': "Sometxt",
    'Language': "Sometxt",
    'Genre': "Sometxt",
    'Pages': "Sometxt",
    'Take_status': "Sometxt",
}

empty_book = {
    'Title': "",
    'Author': "",
    'Country': "",
    'Language': "",
    'Genre': "",
    'Pages': "",
    'Take_status': "",
}


class LibraryCase(unittest.TestCase):
    def test_ValidBook_false(self):
        self.assertEqual(TestProgram.Library.ValidBook(str_book_false), False)

    def test_ValidBook_true(self):
        self.assertEqual(TestProgram.Library.ValidBook(str_book_true), True)

    def test_SearchBook_1(self):
        self.assertEqual(TestProgram.Library.SearchBook(empty_book),
                         TestProgram.Library.books)

    def test_SearchBook_2(self):
        self.assertEqual(TestProgram.Library.SearchBook(book), [])

    def test_AddBook_true(self):
        self.assertEqual(TestProgram.Library.AddBook(str_book_true), True)

    def test_AddBook_false(self):
        self.assertEqual(TestProgram.Library.AddBook(str_book_false), False)

    def test_ProgramLoop(self):
        self.assertEqual(TestProgram.ProgramLoop(), True)

    def test_PrintCase(self):
        self.assertEqual(TestProgram.PrintCase(), True)

    def test_TakeCase(self):
        self.assertEqual(TestProgram.TakeCase(), False)

    def test_ReturnCase(self):
        self.assertEqual(TestProgram.ReturnCase(), False)

    def test_AddCase_false(self):
        self.assertEqual(TestProgram.AddCase(), False)

    def test_SearchCase_false(self):
        self.assertEqual(TestProgram.SearchCase(), False)

    def test_extract_false(self):
        self.assertEqual(TestJson.extract_from_csv("Test.csv"), [])


if __name__ == '__main__':
    unittest.main()
