class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = True

    def check_out(self):
        self.is_checked_out = True

    def check_in(self):
        self.is_checked_out = False


class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        book.check_out()
        self.checked_out_books.append(book)

    def return_book(self, book):
        if book in self.checked_out_books:
            book.check_in()
            self.checked_out_books.remove(book)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        for book in self.books:
            if not book.is_checked_out:
                print(f"'{book.title}' by {book.author}")

    def print_checked_out_books(self):
        for book in self.books:
            if book.is_checked_out:
                print(f"'{book.title}' by {book.author}")


if __name__ == '__main__':
    # Create library
    library = Library()

    # Create books
    book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create patrons
    patron1 = Patron("Alice")
    patron2 = Patron("Bob")

    # Check out books
    patron1.check_out_book(book1)
    patron1.check_out_book(book2)
    patron2.check_out_book(book2)

    # Return books
    patron1.return_book(book1)
    patron1.return_book(book3)

    # Print available and checked out books in the library
    library.print_books()
    library.print_checked_out_books()
