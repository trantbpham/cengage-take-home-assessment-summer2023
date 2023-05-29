# Run the test file via the terminal: python3 program_1_test.py program_1_{#}.py

import unittest
from io import StringIO
from contextlib import redirect_stdout
#Dynamically load these modules
import importlib

#importlib allows for me to run each test case 3 times once per program file in one test case
class BookTests(unittest.TestCase):

    def setUp(self):
        self.files = ['program_1','program_2','program_3',]

    def test_check_out(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            book.check_out()
            self.assertTrue(book.is_checked_out)

    def test_check_out_already_checked_out(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            book.check_out()
            with redirect_stdout(StringIO()) as context:
                book.check_out()
            if context.getvalue().strip() != "Book 'Title' is already checked out.":
                print(file,"did not properly check status before checking out")
            self.assertTrue(book.is_checked_out)

    def test_check_in(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            book.check_out()
            book.check_in()
            self.assertFalse(book.is_checked_out)

    def test_check_in_already_checked_in(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            # Never properly checks if book is already checked in based on test logic
            with redirect_stdout(StringIO()):
                book.check_in()
            self.assertFalse(book.is_checked_out)


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
            except AssertionError as e: self.verificationErrors.append(("PATRON TEST CHECK OUT", str(e)))

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
            except AssertionError as e: self.verificationErrors.append(("PATRON CHECK OUT MAX DIFF", str(e)))

    def test_return_book(self):
        for file in self.files:
            module = importlib.import_module(file)
            book = module.Book("Title", "Author")
            patron = module.Patron("Alice")
            patron.check_out_book(book)
            patron.return_book(book)
            try:
                self.assertNotIn(book, patron.checked_out_books)
            except AssertionError as e: self.verificationErrors.append(("PATRON RETURN BOOK", str(e)))

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
            except AssertionError as e: self.verificationErrors.append(("PATRON RETURN BOOK NOT CHECK OUT", str(e)))

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
            self.assertIn(book, library.books)

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
            except AssertionError as e: self.verificationErrors.append(("LIBRARY PRINT BOOKS", str(e)))
            try:
                self.assertIn(f"'{book2.title}' by {book2.author}", output.getvalue())
            except AssertionError as e: self.verificationErrors.append(("LIBRARY PRINT BOOKS", str(e)))


if __name__ == '__main__':
    unittest.main()
