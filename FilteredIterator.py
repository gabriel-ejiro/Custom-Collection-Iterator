class FilteredIterator:
    def __init__(self, books, *, author=None, category=None):
        self._filtered = [
            book for book in books
            if (author is None or book.author == author)
            and (category is None or book.category == category)
        ]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._filtered):
            book = self._filtered[self._index]
            self._index += 1
            return book
        raise StopIteration
