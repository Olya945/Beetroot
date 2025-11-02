''' Task 2

Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books

'''

class Author:
    # Книги конкретного автора
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    
    def __str__(self):
        return f'Author: {self.name}, was born in {self.birthday} in {self.country}'
    
    def __repr__(self):
        return f'Author(name={self.name!r}, country={self.country!r}, birthday={self.birthday!r})'

class Book:
    # Всі книги в програмі 
    total_books = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1
    
    def __str__(self):
        return f'Book: {self.name} {self.year} by {self.author.name}'
    
    def __repr__(self):
        return f'Book(name={self.name!r}, year={self.year!r}, author={self.author.name!r})'


class Library:
    # Всі книги в бібліотеці
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
    
    # Додавання до списку автора та книги
    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        author.books.append(book)
        return book

    # Отримання всіх книг автора
    def group_by_author(self, author):
        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
        return result
    
    # Отримання всіх книг певного року
    def group_by_year(self, year):
        result = []
        for book in self.books:
            if book.year == year:
                result.append(book)
        return result

    def __str__(self):
        return f'Library: {self.name} ({len(self.books)} books)'
    
    def __repr__(self):
        return f'Library(name={self.name!r}, books={len(self.books)})'
    
