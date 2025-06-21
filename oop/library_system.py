class Book:
    # Base class representing a generic book.
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    # Derived class representing an electronic book.
    # Inherits from Book and adds file size.
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size       # Additional attribute for EBook

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book and adds page count.
    """
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)   # Call base class constructor
        self.page_count = page_count      # Additional attribute for PrintBook

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Composition class representing a library.
    Manages a collection of books (Book, EBook, PrintBook).
    """
    def __init__(self):
        self.books = []  # Store book objects here

    def add_book(self, book):
        # Adds any book type to the library (Book, EBook, PrintBook).
        self.books.append(book)

    def list_books(self):
    
        # Lists the details of all books in the library.
        for book in self.books:
            print(book.get_details())
