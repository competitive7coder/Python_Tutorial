# Aggregation = Represents a relationship where one object (the whole)
# contains references to one or more INDEPENDENT objects (the parts).

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Create Library
library = Library("New York Public Library")

# Create Book objects independently
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("The Colour of Magic", "Terry Pratchett")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Print library name
print(library.name)

# Print all books
#print(library.list_books())
for book in library.list_books():
    print(book)