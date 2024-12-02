# Topic 1: Classes and Objects
# Exercise 1: Definition of a simple class

# Create a class called Product.

# The Product class should have two attributes: name and price.

# The class should have an __init__ method that initializes these attributes.

# Create an instance of the Product class with a name and a price, and display its attributes.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product('Tv set', 250)     ## Instantiate the class
print(product1.name, product1.price)   ## Call the class attributes

