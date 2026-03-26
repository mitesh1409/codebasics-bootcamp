from exceptions.ItemAlreadyBorrowed import ItemAlreadyBorrowed
from exceptions.ItemAlreadyReturned import ItemAlreadyReturned

class LibraryItem:
    def __init__(self, title, is_borrowed):
        self.title = title
        self.is_borrowed = is_borrowed

    def borrow_item(self):
        if self.is_borrowed:
            raise ItemAlreadyBorrowed(f'{self.title} is already borrowed')
        self.is_borrowed = True

    def return_item(self):
        if not self.is_borrowed:
            raise ItemAlreadyReturned(f'{self.title} is already returned')
        self.is_borrowed = False

    def availability(self):
        return 'Not Available' if self.is_borrowed else 'Available'
