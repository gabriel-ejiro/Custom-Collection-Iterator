class PaginatedIterator:
    def __init__(self, books, page_size):
        self._books = books
        self._page_size = page_size
        self._current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        start = self._current_page * self._page_size
        end = start + self._page_size
        if start < len(self._books):
            self._current_page += 1
            return self._books[start:end]
        raise StopIteration
