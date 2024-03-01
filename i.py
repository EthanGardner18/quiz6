class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class GuestInterface:
    def search_book(self, title=None, author=None, genre=None):
        print("Guest is searching for a book")
        pass


class LibrarianInterface:
    def add_book(self, book):
        print("Librarian added a book")
        pass

    def remove_book(self, book):
        print("Librarian removed a book")
        pass

    def generate_reports(self):
        print("Librarian generated a report")
        pass


class MemberInterface:
    def borrow_book(self, book):
        print("Member rented a book")
        pass

    def return_book(self, book):
        print("Member is returning a book")
        pass


class Library(GuestInterface, LibrarianInterface, MemberInterface):
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        print("Library is adding book")
        self.catalog.append(book)

    def remove_book(self, book):
        print("Library is removing a book")
        self.catalog.remove(book)

    def search_book(self, title=None, author=None, genre=None):
        print("Searching for a book\nfound book " + title)
        pass

    def borrow_book(self, book):
        print("Borrowing a book")
        pass

    def return_book(self, book):
        print("Returning book")
        pass

    def generate_reports(self):
        print("Generating report")
        pass


if __name__ == "__main__":
    library = Library()

    # Example usage
    librarian = library
    librarian.add_book(Book("Harry Potter", "J.K. Rowling", "Fantasy"))

    guest = library
    guest.search_book(title="Harry Potter")
