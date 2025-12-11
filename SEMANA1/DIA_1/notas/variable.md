# Variables y tipos de datos

## ¿Qué es una variable?
Una variable es un nombre que hace referencia a un valor almacenado en memoria. Debe comenzar con una letra o guion bajo y no puede contener espacios ni caracteres especiales.

```python
contador = 10
_nombre = "Ana"
es_activo = True
```

## Tipos de datos primitivos
- **Enteros (`int`)**: números sin decimales  
    ```python
    edad = 30
    ```
- **Flotantes (`float`)**: números con decimales  
    ```python
    precio = 19.99
    ```
- **Cadenas (`str`)**: texto entre comillas simples o dobles  
    ```python
    mensaje = "Hola, mundo"
    ```
- **Booleanos (`bool`)**: valores lógicos `True` o `False`  
    ```python
    es_valido = False
    ```

## Estructuras de datos
- **Listas (`list`)**: colección ordenada y mutable  
    ```python
    frutas = ["manzana", "banana", "cereza"]
    ```
- **Tuplas (`tuple`)**: colección ordenada e inmutable  
    ```python
    coordenadas = (10, 20)
    ```
- **Diccionarios (`dict`)**: pares clave-valor  
    ```python
    persona = {"nombre": "Luis", "edad": 25}
    ```
- **Conjuntos (`set`)**: colección no ordenada de elementos únicos  
    ```python
    colores = {"rojo", "verde", "azul"}
    ```

## Conversión de tipos
Se pueden convertir valores entre tipos con funciones incorporadas:
```python
numero_str = "42"
numero_int = int(numero_str)      # 42
texto = str(3.14)                 # "3.14"
bandera = bool(0)                 # False
```

## Ejemplo simple:

```python
edad = 30                #int
altura = 1.78            #float
nombre = "Alexis"        #str
activo = True            #bool
frutas = ["mango", "guayaba", "banana"]
libros = {
    "1984": "George Orwell",
    "Cien años de soledad": "Gabriel García Márquez",
    "El Quijote": "Miguel de Cervantes"
}
contraseña = (10, "yosoygoot", "12avenida")
autos = {"Ford Mustang", "Chevrolet Bel Air", "Volkswagen Beetle"}
```

## Buenas prácticas
- Usar nombres descriptivos.
- Respetar la sensibilidad a mayúsculas/minúsculas.
- Elegir el tipo de dato adecuado para cada uso.
- Evitar cambiar el tipo de una variable sin necesidad.

