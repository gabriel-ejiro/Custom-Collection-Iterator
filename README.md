# Custom-Collection-Iterator

 Objective:
 
The goal is to implement a custom collection class and provide an iterator to traverse through its elements using the Iterator Design Pattern. You will learn how to separate collection logic from traversal logic and implement custom iteration behavior.

📘 Domain Story:

A library is creating a digital archive for its book collection.

- The archive allows storing books sorted by categories.

- The system must allow iterating over books in custom ways: for instance, by author, by category, or alphabetically.

- For this project, I will build a custom collection that holds books and use the Iterator Pattern to enable iteration over them.


📋 Functional Requirements:

- Create a Book class with attributes like title, author, and category.

- Create a BookCollection class that manages a list of books.

- Implement a custom Iterator that supports iteration over the collection.

- Demonstrate use of the iterator in a client (main) script.


Class Structure:

- Book	Represents a single book.

- BookCollection	Stores and manages a list of books.
  
- BookIterator	Custom iterator for the book collection.
  
- Main	Client code using the iterator.
