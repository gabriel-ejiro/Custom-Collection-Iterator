class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def get_books(self):
        return self._books

    def __iter__(self):
        return BookIterator(self._books)
