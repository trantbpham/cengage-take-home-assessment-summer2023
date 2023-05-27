# Run the test file via the terminal: python3 program_2_test.py program_2_{#}.py
import unittest
from io import StringIO
from contextlib import redirect_stdout
#Dynamically load these modules
import program_2
import program_2
import program_3

class BookTests(unittest.TestCase):
    def test_check_out(self):
        book = program_2.Book("Title", "Author")
        book.check_out()
        self.assertTrue(book.is_checked_out)

    def test_check_out_already_checked_out(self):
        book = program_2.Book("Title", "Author")
        book.check_out()
        with redirect_stdout(StringIO()):
            book.check_out()
        self.assertTrue(book.is_checked_out)

    def test_check_in(self):
        book = program_2.Book("Title", "Author")
        book.check_out()
        book.check_in()
        self.assertFalse(book.is_checked_out)

    def test_check_in_already_checked_in(self):
        book = program_2.Book("Title", "Author")
        with redirect_stdout(StringIO()):
            book.check_in()
        self.assertFalse(book.is_checked_out)


class PatronTests(unittest.TestCase):
    def test_check_out_book(self):
        book = program_2.Book("Title", "Author")
        patron = program_2.Patron("Alice")
        patron.check_out_book(book)
        self.assertIn(book, patron.checked_out_books)

    def test_check_out_book_reached_limit(self):
        book1 = program_2.Book("Title 1", "Author")
        book2 = program_2.Book("Title 2", "Author")
        book3 = program_2.Book("Title 3", "Author")
        book4 = program_2.Book("Title 4", "Author")
        patron = program_2.Patron("Alice")

        with redirect_stdout(StringIO()):
            patron.check_out_book(book1)
            patron.check_out_book(book2)
            patron.check_out_book(book3)
            patron.check_out_book(book4)

        self.assertNotIn(book4, patron.checked_out_books)

    def test_return_book(self):
        book = program_2.Book("Title", "Author")
        patron = program_2.Patron("Alice")
        patron.check_out_book(book)
        patron.return_book(book)
        self.assertNotIn(book, patron.checked_out_books)

    def test_return_book_not_checked_out(self):
        book = program_2.Book("Title", "Author")
        patron = program_2.Patron("Alice")

        with redirect_stdout(StringIO()):
            patron.return_book(book)

        self.assertNotIn(book, patron.checked_out_books)


class LibraryTests(unittest.TestCase):
    def test_add_book(self):
        book = program_2.Book("Title", "Author")
        library = program_2.Library()
        library.add_book(book)
        self.assertIn(book, library.books)

    def test_print_books(self):
        book1 = program_2.Book("Title 1", "Author")
        book2 = program_2.Book("Title 2", "Author")
        library = program_2.Library()
        library.add_book(book1)
        library.add_book(book2)

        with redirect_stdout(StringIO()) as output:
            library.print_books()

        self.assertIn(f"'{book1.title}' by {book1.author}", output.getvalue())
        self.assertIn(f"'{book2.title}' by {book2.author}", output.getvalue())

    def test_print_checked_out_books(self):
        book1 = program_2.Book("Title 1", "Author")
        book2 = program_2.Book("Title 2", "Author")
        library = program_2.Library()
        library.add_book(book1)
        library.add_book(book2)

        book1.check_out()
        book2.check_out()

        with redirect_stdout(StringIO()) as output:
            library.print_checked_out_books()

        self.assertIn(f"'{book1.title}' by {book1.author}", output.getvalue())
        self.assertIn(f"'{book2.title}' by {book2.author}", output.getvalue())


if __name__ == '__main__':
    unittest.main()
