# Exercise 8: Object Comparison

# Create a class called Person with the attributes name and age.

# Add a method is_older_than that takes another instance of Person as a parameter and returns True if the first person is older than the second, and False otherwise.

# Create two instances of the Person class and compare their ages.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_older_than(self, other: 'Person'):
        return self.age > other.age


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

if person1.is_older_than(person2):
    print(f"{person1.name} is older than {person2.name}")
else:
    print(f"{person1.name} is not older than {person2.name}")