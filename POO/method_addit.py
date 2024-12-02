# Exercise 5: Additional Methods

# Add a method to the Book class called summary that prints a summary of the book in the format "title by author, pages pages".

# Create an instance of the Book class and call the summary method.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

book1 = Book('Harry Potter', 'JK Rowling', 223)

# print(book1.title)
# print(book1.author)
# print(book1.pages)

book1.summary()