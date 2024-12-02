# Exercise 9: Class and Static Methods

# Create a class called Mathematics with a class method sum that takes two numbers and returns their sum.

# Add a static method multiplication that takes two numbers and returns their product.

# Call both methods without creating an instance of the class.


class Mathematics:
    @classmethod
    def sum(cls, a, b):
        return a + b

    @staticmethod
    def multiplication(a, b):
        return a * b

# Calling both methods without creating an instance of the class
print(Mathematics.sum(3, 5))  # Output: 8
print(Mathematics.multiplication(4, 6))  # Output: 24