def main():
    collection = BookCollection()
    collection.add_book(Book("1984", "George Orwell", "Dystopia"))
    collection.add_book(Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"))
    collection.add_book(Book("Clean Code", "Robert C. Martin", "Programming"))
    collection.add_book(Book("The Silmarillion", "J.R.R. Tolkien", "Fantasy"))
    collection.add_book(Book("Brave New World", "Aldous Huxley", "Dystopia"))

    print("📚 Full Library:")
    for book in collection:
        print(book)

    print("\n🔍 Filtered by author (J.R.R. Tolkien):")
    for book in FilteredIterator(collection.get_books(), author="J.R.R. Tolkien"):
        print(book)

    print("\n🔍 Filtered by category (Dystopia):")
    for book in FilteredIterator(collection.get_books(), category="Dystopia"):
        print(book)

    print("\n📚 Sorted by title:")
    for book in SortedIterator(collection.get_books(), by="title"):
        print(book)

    print("\n📚 Reverse order:")
    for book in ReverseIterator(collection.get_books()):
        print(book)

    print("\n📖 Paginated view (2 books per page):")
    for page in PaginatedIterator(collection.get_books(), page_size=2):
        print("Page:")
        for book in page:
            print(f" - {book}")

main()
