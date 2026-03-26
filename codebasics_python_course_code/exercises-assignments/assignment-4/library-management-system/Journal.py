from LibraryItem import LibraryItem

class Journal(LibraryItem):
    def __init__(self, title, is_borrowed, issue_number):
        super().__init__(title, is_borrowed)
        self.issue_number = issue_number

    def __str__(self):
        return f'Journal: {self.title} Issue: {self.issue_number}, {self.availability()}'
