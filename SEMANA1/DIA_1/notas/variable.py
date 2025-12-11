"""
Variables y tipos de datos en Python.

Una variable es un nombre que referencia un valor en memoria.
Debe iniciar con letra o guion bajo, sin espacios ni caracteres especiales.
"""
contador = 10
_nombre = "Ana"
es_activo = True

# Tipos de datos primitivos
edad = 30                  # int
precio = 19.99             # float
mensaje = "Hola, mundo"    # str
es_valido = False          # bool

# Estructuras de datos
frutas = ["manzana", "banana", "cereza"]  # list
coordenadas = (10, 20)                    # tuple
persona = {"nombre": "Luis", "edad": 25}  # dict
colores = {"rojo", "verde", "azul"}       # set

# Conversión de tipos
numero_str = "42"
numero_int = int(numero_str)
texto = str(3.14)
bandera = bool(0)

# Ejemplo simple
edad = 30
altura = 1.78
nombre = "Alexis"
activo = True
frutas = ["mango", "guayaba", "banana"]
libros = {
    "1984": "George Orwell",
    "Cien años de soledad": "Gabriel García Márquez",
    "El Quijote": "Miguel de Cervantes",
}
contraseña = (10, "yosoygroot", "12avenida")
autos = {"Ford Mustang", "Chevrolet Bel Air", "Volkswagen Beetle"}

# Buenas prácticas:
# - Usar nombres descriptivos.
# - Respetar la sensibilidad a mayúsculas/minúsculas.
# - Elegir el tipo de dato adecuado.
# - Evitar cambios innecesarios de tipo.
