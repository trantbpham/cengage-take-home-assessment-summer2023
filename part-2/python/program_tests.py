# Run the test file via the terminal: python3 program_1_test.py program_1_{#}.py
import unittest
import importlib
from io import StringIO
from contextlib import redirect_stdout


program_module = None


def load_module(module_name):
    global program_module
    program_module = importlib.import_module(module_name)

# Define test classes


class BookTests(unittest.TestCase):
    def setUp(self):
        self.program = program_module

    def load_module(self, module_name):
        self.program = importlib.import_module(module_name)

    def test_check_out(self):
        book = self.program.Book("Title", "Author")
        book.check_out()
        self.assertTrue(book.is_checked_out)

    def test_check_out_already_checked_out(self):
        book = self.program.Book("Title", "Author")
        book.check_out()
        with redirect_stdout(StringIO()):
            book.check_out()
        self.assertTrue(book.is_checked_out)

    def test_check_in(self):
        book = self.program.Book("Title", "Author")
        book.check_out()
        book.check_in()
        self.assertFalse(book.is_checked_out)

    def test_check_in_already_checked_in(self):
        book = self.program.Book("Title", "Author")
        with redirect_stdout(StringIO()):
            book.check_in()
        self.assertFalse(book.is_checked_out)


class PatronTests(unittest.TestCase):
    def test_check_out_book(self):
        book = self.program.Book("Title", "Author")
        patron = self.program.Patron("Alice")
        patron.check_out_book(book)
        self.assertIn(book, patron.checked_out_books)

    def test_check_out_book_reached_limit(self):
        book1 = self.program.Book("Title 1", "Author")
        book2 = self.program.Book("Title 2", "Author")
        book3 = self.program.Book("Title 3", "Author")
        book4 = self.program.Book("Title 4", "Author")
        patron = self.program.Patron("Alice")

        with redirect_stdout(StringIO()):
            patron.check_out_book(book1)
            patron.check_out_book(book2)
            patron.check_out_book(book3)
            patron.check_out_book(book4)

        self.assertNotIn(book4, patron.checked_out_books)

    def test_return_book(self):
        book = self.program.Book("Title", "Author")
        patron = self.program.Patron("Alice")
        patron.check_out_book(book)
        patron.return_book(book)
        self.assertNotIn(book, patron.checked_out_books)

    def test_return_book_not_checked_out(self):
        book = self.program.Book("Title", "Author")
        patron = self.program.Patron("Alice")

        with redirect_stdout(StringIO()):
            patron.return_book(book)

        self.assertNotIn(book, patron.checked_out_books)


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.program = None

    def load_module(self, module_name):
        self.program = importlib.import_module(module_name)

    def test_add_book(self):
        book = self.program.Book("Title", "Author")
        library = self.program.Library()
        library.add_book(book)
        self.assertIn(book, library.books)

    def test_print_books(self):
        book1 = self.program.Book("Title 1", "Author")
        book2 = self.program.Book("Title 2", "Author")
        library = self.program.Library()
        library.add_book(book1)
        library.add_book(book2)

        with redirect_stdout(StringIO()) as output:
            library.print_books()

        self.assertIn(f"'{book1.title}' by {book1.author}", output.getvalue())
        self.assertIn(f"'{book2.title}' by {book2.author}", output.getvalue())

    def test_print_checked_out_books(self):
        book1 = self.program.Book("Title 1", "Author")
        book2 = self.program.Book("Title 2", "Author")
        library = self.program.Library()
        library.add_book(book1)
        library.add_book(book2)

        book1.check_out()
        book2.check_out()

        with redirect_stdout(StringIO()) as output:
            library.print_checked_out_books()

        self.assertIn(f"'{book1.title}' by {book1.author}", output.getvalue())
        self.assertIn(f"'{book2.title}' by {book2.author}", output.getvalue())


# Define the test suite
def suite():
    suite = unittest.TestSuite()

    # Add tests here
    suite.addTest(BookTests())
    suite.addTest(PatronTests())
    suite.addTest(LibraryTests())

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    # Load each program and run tests
    for program_number in range(1, 4):
        module_name = f"program_{program_number}"
        print(f"Running tests for {module_name}:")
        load_module(module_name)

        for test_case in [BookTests, PatronTests, LibraryTests]:
            suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
            runner.run(suite)
