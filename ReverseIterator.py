class ReverseIterator:
    def __init__(self, books):
        self._books = books
        self._index = len(books) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 0:
            book = self._books[self._index]
            self._index -= 1
            return book
        raise StopIteration
