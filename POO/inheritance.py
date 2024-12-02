# Create a system for a school with two main classes: Person and Student.
# Person will have two attributes: name and age, and a method 'show_info' that prints the name and age of the person.
# Student will inherit from the Person class and have an additional attribute: grade, and a method 'show_age' that prints the student's grade.
# Create an instance of the Student class and print its attributes, use the methods to ensure everything works well.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old!")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_age(self):
        print(f"Age: {self.grade}")

student1 = Student('Robert', 28, '7mo')

student1.show_info()
student1.show_age()