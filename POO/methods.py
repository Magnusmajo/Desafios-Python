# Exercise 2: Class Methods

# Add a method to the Product class called show_info that prints the name and price of the product.

# Create two instances of the Product class and call the show_info method for each one.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name} = ${self.price}")

product1 = Product('Tv set', 250)
product2 = Product('Acer notebook', 859)

product1.show_info()
product2.show_info()