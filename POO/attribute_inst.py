# Exercise 4: Instance Attributes

# Create a class called Book with the attributes title, author, and pages.

# Add an __init__ method to initialize these attributes.

# Create an instance of the Book class and display its attributes.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book('Harry Potter', 'JK Rowling', 223)

print(book1.title)
print(book1.author)
print(book1.pages)