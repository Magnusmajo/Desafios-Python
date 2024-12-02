# Exercise 10: Object Representation

# Modify the Product class to have a __str__ method that returns a string representing the product in the format "Name: name, Price: price".

class Producto:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio

	def __str__(self):
		return f"Nombre: {self.nombre}, Precio: {self.precio}"

# Crea una instancia de la clase y muestra su representación usando print.
producto = Producto("Manzana", 0.75)
print(producto)