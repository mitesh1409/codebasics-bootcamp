from LibraryItem import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, is_borrowed, author):
        super().__init__(title, is_borrowed)
        self.author = author

    def __str__(self):
        return f'Book: {self.title} by {self.author}, {self.availability()}'
