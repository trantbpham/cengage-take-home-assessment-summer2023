# Run the test file via the terminal: python3 program_1_test.py program_1_{#}.py
import unittest
from io import StringIO
from contextlib import redirect_stdout
#Dynamically load these modules
import importlib
#importlib allows for me to run each test case with all programs in self.files as one test.
#if an assertion error happens within the try block we append it to the error list instead of throwing after first fail,
#then after all test have been run, the error list will show the failed test cases and which program it failed with
class BookTests(unittest.TestCase):

    def setUp(self):
        self.files = ['program_1','program_2','program_3',]
        self.verificationErrors = []
        self.maxDiff = None

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_check_out(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            book.check_out()
            try:
                self.assertTrue(book.is_checked_out)
            except AssertionError as e: self.verificationErrors.append((file,"BOOK TEST CHECK OUT", str(e)))

    def test_check_out_already_checked_out(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            book.check_out()
            with redirect_stdout(StringIO()) as context:
                book.check_out()
            #technically works on program 3 but does not check if book is already check out before doing so
            if context.getvalue().strip() != "Book 'Title' is already checked out.":
                print(file,"did not properly check status before checking out")
            try:
                self.assertTrue(book.is_checked_out)
            except AssertionError as e: self.verificationErrors.append((file,"BOOK ALREADY CHECKED OUT", str(e)))

    def test_check_in(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            book.check_out()
            book.check_in()
            try:
                self.assertFalse(book.is_checked_out)
            except AssertionError as e: self.verificationErrors.append((file,"BOOK TEST CHECK IN", str(e)))

    def test_check_in_already_checked_in(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            # Never properly checks if book is already checked in based on test logic
            with redirect_stdout(StringIO()):
                book.check_in()
            try:
                self.assertFalse(book.is_checked_out)
            except AssertionError as e: self.verificationErrors.append((file,"BOOK TEST ALREADY CHECKED IN", str(e)))


class PatronTests(unittest.TestCase):

    def setUp(self):
        self.files = ['program_1','program_2','program_3']
        self.verificationErrors = []
        self.maxDiff = None

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_check_out_book(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            patron = module.Patron("Alice")
            patron.check_out_book(book)
            try:
                self.assertIn(book, patron.checked_out_books)
            except AssertionError as e: self.verificationErrors.append((file,"PATRON TEST CHECK OUT", str(e)))

    def test_check_out_book_reached_limit(self):
        for file in self.files:
            module = importlib.import_module(file)
            book1 = module.Book("Title 1", "Author")
            book2 = module.Book("Title 2", "Author")
            book3 = module.Book("Title 3", "Author")
            book4 = module.Book("Title 4", "Author")
            patron = module.Patron("Alice")

            with redirect_stdout(StringIO()):
                patron.check_out_book(book1)
                patron.check_out_book(book2)
                patron.check_out_book(book3)
                patron.check_out_book(book4)

            try:
                self.assertNotIn(book4, patron.checked_out_books)
            except AssertionError as e: self.verificationErrors.append((file,"PATRON CHECK OUT MAX DIFF", str(e)))

    def test_return_book(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            patron = module.Patron("Alice")
            patron.check_out_book(book)
            patron.return_book(book)
            try:
                self.assertNotIn(book, patron.checked_out_books)
            except AssertionError as e: self.verificationErrors.append((file,"PATRON RETURN BOOK", str(e)))

    def test_return_book_not_checked_out(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            patron = module.Patron("Alice")

            with redirect_stdout(StringIO()) as context:
                patron.return_book(book)
            print(context.getvalue().strip())
            try:
                self.assertNotIn(book, patron.checked_out_books)
            except AssertionError as e: self.verificationErrors.append((file,"PATRON RETURN BOOK NOT CHECK OUT", str(e)))

class LibraryTests(unittest.TestCase):

    def setUp(self):
        self.files = ['program_1','program_2','program_3']
        self.verificationErrors = []
        self.maxDiff = None

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_add_book(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            library = module.Library()
            library.add_book(book)
            try:
                self.assertIn(book, library.books)
            except AssertionError as e: self.verificationErrors.append((file,"LIBRARY TEST ADD BOOKS", str(e)))

    def test_print_books(self):
        for file in self.files:
            module = importlib.import_module(file)

            book1 = module.Book("Title 1", "Author")
            book2 = module.Book("Title 2", "Author")
            library = module.Library()
            library.add_book(book1)
            library.add_book(book2)

            with redirect_stdout(StringIO()) as output:
                library.print_books()
            try:
                self.assertIn(f"'{book1.title}' by {book1.author}", output.getvalue())
            except AssertionError as e: self.verificationErrors.append((file,"LIBRARY PRINT BOOKS", str(e)))
            try:
                self.assertIn(f"'{book2.title}' by {book2.author}", output.getvalue())
            except AssertionError as e: self.verificationErrors.append((file,"LIBRARY PRINT BOOKS", str(e)))

    def test_print_checked_out_books(self):
        for file in self.files:
            print(file)
            module = importlib.import_module(file)
            book1 = module.Book("Title 1", "Author")
            book2 = module.Book("Title 2", "Author")
            library = module.Library()
            library.add_book(book1)
            library.add_book(book2)

            book1.check_out()
            book2.check_out()

            with redirect_stdout(StringIO()) as output:
                library.print_checked_out_books()

            try:
                self.assertIn(f"'{book1.title}' by {book1.author}", output.getvalue())
            except AssertionError as e: self.verificationErrors.append((file,"LIBRARY PRINT BOOKS", str(e)))
            try:
                self.assertIn(f"'{book2.title}' by {book2.author}", output.getvalue())
            except AssertionError as e: self.verificationErrors.append((file,"LIBRARY PRINT BOOKS", str(e)))


if __name__ == '__main__':
    unittest.main()
