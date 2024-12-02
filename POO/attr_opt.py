# Exercise 6: Optional Attributes

# Modify the Product class to have an optional attribute description that defaults to an empty string.

# Modify the show_info method to also display the description if it is present.

# Create two instances of the Product class, one with a description and one without, and call the show_info method for each.

class Product:
    def __init__(self, name, price, description=""):
        self.name = name
        self.price = price
        self.description = description

    def show_info(self):
        print(f"{self.name} = ${self.price}")
        if self.description:
            print(f"Description: {self.description}")

product1 = Product('Tv set', 250)
product2 = Product('Acer notebook', 859, 'Is really good')

product1.show_info()
product2.show_info()
