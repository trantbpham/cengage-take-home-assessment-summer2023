class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"Book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"Book '{self.title}' is already checked out.")

    def check_in(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Book '{self.title}' has been checked in.")
        else:
            print(f"Book '{self.title}' is already checked in.")


class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        if len(self.checked_out_books) >= 3:
            print(f"{self.name} has reached the maximum limit of checked out books.")
        else:
            book.check_out()
            self.checked_out_books.append(book)

    def return_book(self, book):
        if book in self.checked_out_books:
            book.check_in()
            self.checked_out_books.remove(book)
        else:
            print(f"{self.name} does not have '{book.title}' checked out.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        print("Available Books:")
        for book in self.books:
            if not book.is_checked_out:
                print(f"- '{book.title}' by {book.author}")

    def print_checked_out_books(self):
        print("Checked Out Books:")
        for book in self.books:
            if book.is_checked_out:
                print(f"- '{book.title}' by {book.author}")


# Example usage
if __name__ == '__main__':
    # Create books
    book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    # Create library
    library = Library()

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