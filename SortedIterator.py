class SortedIterator:
    def __init__(self, books, by="title"):
        self._sorted = sorted(books, key=lambda book: getattr(book, by))
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sorted):
            book = self._sorted[self._index]
            self._index += 1
            return book
        raise StopIteration
