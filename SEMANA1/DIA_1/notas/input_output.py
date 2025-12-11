# Entrada y Salida en Python

Este documento explica de forma clara y completa cómo funcionan **la entrada y la salida de datos** en Python. Puedes copiarlo y pegarlo dentro de un archivo `.py` como comentario o usarlo como guía de estudio.

---

## 1. ¿Qué es la Entrada y la Salida?

'''En programación, **entrada (input)** es cualquier información que el usuario proporciona, y **salida (output)** es la información que el programa muestra al usuario.

Python facilita ambas tareas a través de dos funciones principales:

* `input()` → Para recibir datos del usuario.
* `print()` → Para mostrar información en pantalla.'''

---

## 2. `input()`: Recibir datos del usuario

'''La función `input()` le pide al usuario que escriba algo. Siempre devuelve un **string (cadena de texto)**.'''

# Sintaxis


variable = input("Mensaje para el usuario: ")


#  Ejemplo básico


nombre = input("Tu nombre: ")


'''Esto detiene el programa hasta que el usuario escriba algo y presione Enter.'''

### ✔ Resultado:

''' Si el usuario escribe: `Alexis`
* Entonces la variable `nombre` contiene: "Alexis"'''


## 3. `print()`: Mostrar información

'''La función `print()` se usa para mostrar cualquier texto o valor en la pantalla.'''

### 📌 Sintaxis


print(valor1, valor2, ...)

### 📌 Ejemplo básico


print("Hola", nombre)


'''Esto muestra:


Hola Alexis'''


print()    # separa automáticamente los valores por un espacio.


## 4. Unir Entrada y Salida

nombre = input("Tu nombre: ")
print("Hola", nombre)

'''Este es el programa más simple que interactúa con un usuario.'''

## 5. Convertir tipos de datos

# Recuerda: **`input()` siempre devuelve texto**. Si necesitas números, debes convertirlos.

### Convertir a entero

edad = int(input("Tu edad: "))

### Convertir a flotante

peso = float(input("Tu peso: "))


## 6. Mejorar la salida con f-strings

''' Los **f-strings** son la forma moderna y clara de formatear texto en Python.'''

### Ejemplo


nombre = input("Tu nombre: ")
print(f"Hola {nombre}, bienvenido!")

## 7. Ejemplos prácticos adicionales

### Ejemplo 1: Sumar dos números

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
resultado = a + b
print(f"La suma es {resultado}")


###  Ejemplo 2: Mensaje personalizado


ciudad = input("¿Dónde vives? ")
print(f"Perfecto, {nombre}, veo que vives en {ciudad}")

## 8. Resumen

''' `input()` → captura texto
* `print()` → muestra texto
* Debes **convertir tipos** si necesitas números
* f-strings → salida elegante y clara
'''
