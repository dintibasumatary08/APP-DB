 # Class for Book
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Book ID: {self.book_id}, Title: {self.title}, "
              f"Author: {self.author}, Status: {status}")


# Class for Patron
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


# Class for Library
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.available:
                book.available = False
                patron.borrowed_books.append(book.title)
                print(f"{patron.name} borrowed '{book.title}'.")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid Patron ID or Book ID.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.title in patron.borrowed_books:
                patron.borrowed_books.remove(book.title)
                book.available = True
                print(f"{patron.name} returned '{book.title}'.")
            else:
                print("This patron did not borrow this book.")
        else:
            print("Invalid Patron ID or Book ID.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            book.display()

    # Display all patrons
    def display_patrons(self):
        print("\nLibrary Patrons:")
        for patron in self.patrons.values():
            patron.display()
            print()


# Main Program
library = Library()

# Adding Books
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Mark Lee"))
library.add_book(Book(103, "Machine Learning", "Andrew Ng"))

# Registering Patrons
library.register_patron(Patron(1, "Alice"))
library.register_patron(Patron(2, "Bob"))

# Display Books
library.display_books()

# Borrow Books
library.borrow_book(1, 101)
library.borrow_book(2, 102)

# Display Books After Borrowing
library.display_books()

# Return Book
library.return_book(1, 101)

# Display Books After Returning
library.display_books()

# Display Patrons
library.display_patrons()