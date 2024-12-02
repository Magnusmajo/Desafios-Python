
![image](https://github.com/user-attachments/assets/b7a00f69-cd62-40ca-b5ac-fa70c74d02ce)

# POO

La Programación Orientada a Objetos (POO) es un paradigma de programación que utiliza "objetos" para modelar datos y comportamientos. En Python, la POO se implementa mediante clases y objetos.

## Conceptos Clave

- **Clase**: Es una plantilla para crear objetos. Define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán.
- **Objeto**: Es una instancia de una clase. Cada objeto puede tener diferentes valores para los atributos definidos en la clase.
- **Atributo**: Es una variable que pertenece a una clase o a un objeto.
- **Método**: Es una función que pertenece a una clase o a un objeto.

## Ejemplo Básico

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar()
```

En este ejemplo, `Persona` es una clase con un constructor `__init__` que inicializa los atributos `nombre` y `edad`. El método `saludar` imprime un saludo utilizando estos atributos. `persona1` es un objeto de la clase `Persona`.

## Ventajas de la POO

- **Modularidad**: El código se organiza en clases, lo que facilita su mantenimiento y reutilización.
- **Abstracción**: Permite ocultar detalles complejos y mostrar solo la funcionalidad esencial.
- **Encapsulamiento**: Los datos y métodos están encapsulados dentro de las clases, lo que protege los datos de modificaciones no autorizadas.
- **Herencia**: Las clases pueden heredar atributos y métodos de otras clases, lo que permite reutilizar código y crear jerarquías de clases.
- **Polimorfismo**: Permite que diferentes clases sean tratadas como instancias de una misma clase a través de una interfaz común.

La POO es una herramienta poderosa en Python que permite escribir código más claro, modular y fácil de mantener.

## Práctica: 

### Ejercicio 1: Clases y Objetos Básicos

#### Exercise 1: Definition of a simple class

Create a class called Product.

The Product class should have two attributes: name and price.

The class should have an __init__ method that initializes these attributes.

Create an instance of the Product class with a name and a price, and display its attributes.

#### Exercise 2: Class Methods

Add a method to the Product class called show_info that prints the name and price of the product.

Create two instances of the Product class and call the show_info method for each one.

####  Exercise 3: Basic Operations

Create a class called BankAccount with the attributes holder and balance.

Add methods to deposit and withdraw money from the account, and a method to check_balance.

Create an instance of the class and perform some deposit and withdrawal operations, showing the balance after each operation.

####  Exercise 4: Instance Attributes

Create a class called Book with the attributes title, author, and pages.

Add an __init__ method to initialize these attributes.

Create an instance of the Book class and display its attributes.

####  Exercise 5: Additional Methods

Add a method to the Book class called summary that prints a summary of the book in the format "title by author, pages pages".

Create an instance of the Book class and call the summary method.

####  Exercise 6: Optional Attributes

Modify the Product class to have an optional attribute description that defaults to an empty string.

Modify the show_info method to also display the description if it is present.

Create two instances of the Product class, one with a description and one without, and call the show_info method for each.

####  Exercise 7: Update Methods

Add a method to the BankAccount class called update_holder that allows changing the account holder's name.

Create an instance of the class, change the account holder's name, and display the balance and the new holder.

####  Exercise 8: Object Comparison

Create a class called Person with the attributes name and age.

Add a method is_older_than that takes another instance of Person as a parameter and returns True if the first person is older than the second, and False otherwise.

Create two instances of the Person class and compare their ages.

####  Exercise 9: Class and Static Methods

Create a class called Mathematics with a class method sum that takes two numbers and returns their sum.

Add a static method multiplication that takes two numbers and returns their product.

Call both methods without creating an instance of the class.

####  Exercise 10: Object Representation

Modify the Product class to have a __str__ method that returns a string representing the product in the format "Name: name, Price: price".

--  

Author: Alexis Rodriguez Rodriguez  
Date: Dec-2024  
This is an public project to practice. I hope you all find it useful.
