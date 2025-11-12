class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = 'available'

    def __str__(self):
        return f'"{self.title}" by {self.author} - {self.status}'
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Added book: {book.title}')

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.status == 'available':
                    book.status = 'borrowed'
                    print(f'You borrowed: {book.title}!')
                    return
                else:
                    print(f'Sorry, {title} is already borrowed!')
                    return
        print(f'{book.title} not found!')

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.status == "borrowed":
                    book.status = "available"
                    print(f'You returned: {book.title}')
                    return
                else:
                    print(f'"{title}" was not borrowed.')
                    return
        print(f'Book "{title}" not found.')

    @property
    def list_available(self):
        print('Available books:')
        for book in self.books:
            if book.status == 'available':
                print(f' - {book.title} by {book.author}')
        print()

book1 = Book("Python Basics", "Thuan")
book2 = Book("OOP in Depth", "Kiet")
book3 = Book("AI Revolution", "Quan")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_available

library.borrow_book("OOP in Depth")
library.borrow_book("AI Revolution")

library.list_available

library.return_book("OOP in Depth")
library.list_available