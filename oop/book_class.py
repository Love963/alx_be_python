class Book:
    # A class to represent a book using Python magic methods.
    def __init__(self, title: str, author: str, year: int):
        # Constructor (__init__):
        # Initializes the book's title, author, and publication year.
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor (__del__):
        Called when the object is about to be destroyed.
        Prints a message indicating the book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Informal string representation (__str__):
        Returns a user-friendly description of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation (__repr__):
        Returns a string that could recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
