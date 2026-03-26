import traceback

from Book import Book
from Journal import Journal
from exceptions.ItemAlreadyBorrowed import ItemAlreadyBorrowed
from exceptions.ItemAlreadyReturned import ItemAlreadyReturned

a_book = Book("The Magic of Thinking Big", False, "David Schwartz")

print(a_book)

try:
    a_book.borrow_item()
    a_book.borrow_item()
except ItemAlreadyBorrowed as ex:
    print('An error occurred', ex)
    traceback.print_exc()
finally:
    print(f'Request to borrow {a_book.title} book is settled')

a_journal = Journal('Nature', False, 50)

print(a_journal)

try:
    a_journal.return_item()
except ItemAlreadyReturned as ex:
    print('An error occurred', ex)
    traceback.print_exc()
finally:
    print(f'Request to return {a_journal.title} journal is settled')
