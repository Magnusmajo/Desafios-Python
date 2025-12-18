# Funciones (pensar como desarrollador)

## Teoría esencial

### 1. ¿Qué es una función?
Una **función** es un bloque de código **reutilizable** que encapsula una tarea concreta. Sirve para:
- **Evitar repetición** (DRY: *Don’t Repeat Yourself*).
- **Organizar** el programa en piezas pequeñas y mantenibles.
- **Abstraer** detalles: describes *qué* quieres hacer, no *cómo* en cada lugar.
- **Probar** y depurar más fácil (las funciones se testean por separado).

**Cómo pensar como desarrollador:** cuando veas un patrón repetido o un proceso con pasos claros, probablemente merece una función.

Ejemplo mental:
- “Calcular el total con impuestos”
- “Validar un email”
- “Formatear un mensaje”
Cada una es una tarea que puede convertirse en una función.

---

### 2. Sintaxis básica
En Python, una función se define con `def`, un nombre, paréntesis y dos puntos. El cuerpo va indentado.

```python
def saludar():
    print("Hola")
```

Luego se **llama** (ejecuta) así:

```python
saludar()
```

**Puntos clave:**
- El nombre debería ser **descriptivo** (verbo + objetivo): `calcular_total`, `validar_usuario`.
- La indentación es obligatoria.
- Una función puede tener 0 o más parámetros.

---

### 3. Funciones con parámetros
Los **parámetros** permiten que la función reciba datos externos para trabajar con ellos.

```python
def saludar(nombre):
    print(f"Hola, {nombre}")
```

Uso:

```python
saludar("Ana")
saludar("Carlos")
```

**Vocabulario importante:**
- **Parámetro**: variable en la definición (`nombre`).
- **Argumento**: valor al llamar (`"Ana"`).

Múltiples parámetros:

```python
def sumar(a, b):
    print(a + b)

sumar(3, 5)
```

Parámetros por posición vs por nombre:
```python
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentar("Lucía", 20)          # por posición
presentar(edad=20, nombre="Lucía")  # por nombre (keyword arguments)
```

---

### 4. Funciones que retornan valores
Muchas funciones no solo muestran resultados, sino que **devuelven** un valor usando `return`. Esto permite usar el resultado en otras partes del programa.

```python
def suma(a, b):
    return a + b

resultado = suma(10, 5)
print(resultado)  # 15
```

Ejemplo de encadenar resultados:
```python
def aplicar_iva(precio, iva=0.21):
    return precio * (1 + iva)

total = aplicar_iva(100)
descuento = total * 0.10
print(total - descuento)
```

**Detalles importantes de `return`:**
- Termina la función inmediatamente.
- Puede devolver cualquier tipo: `int`, `float`, `str`, `list`, `dict`, etc.
- Puede devolver **varios valores** (en realidad una tupla):

```python
def dividir(a, b):
    cociente = a // b
    resto = a % b
    return cociente, resto

c, r = dividir(10, 3)
print(c, r)  # 3 1
```

---

### 5. Diferencia clave
La diferencia clave suele ser entre **imprimir** y **retornar**:

- `print()` **muestra** algo en pantalla (sirve para depurar o informar).
- `return` **devuelve** un valor para que el programa lo use.

Ejemplo:

```python
def cuadrado_print(x):
    print(x * x)

def cuadrado_return(x):
    return x * x
```

Uso:
```python
a = cuadrado_print(4)   # imprime 16, pero a será None
b = cuadrado_return(4)  # b será 16
print(a)  # None
print(b)  # 16
```

**Regla práctica:** si necesitas el resultado para seguir calculando, usa `return`. Si solo necesitas mostrar información al usuario, usa `print()`.

---

### 6. Parámetros por defecto
Puedes asignar valores por defecto a parámetros. Si no se pasa ese argumento, se usa el valor por defecto.

```python
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}")

saludar()           # Hola, Invitado
saludar("Marta")    # Hola, Marta
```

Ejemplo realista:
```python
def calcular_total(subtotal, iva=0.21, descuento=0.0):
    return subtotal * (1 + iva) * (1 - descuento)

print(calcular_total(100))                 # sin descuento
print(calcular_total(100, descuento=0.10)) # con descuento
```

**Cuidado importante (mutables):**
No uses listas/diccionarios como valor por defecto si los vas a modificar:

❌ Mal:
```python
def agregar_item(item, lista=[]):
    lista.append(item)
    return lista
```

✅ Bien:
```python
def agregar_item(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

---

### 7. Buenas prácticas
- **Nombres claros**: `calcular_promedio()` es mejor que `cp()`.
- **Una responsabilidad por función**: que haga una sola cosa bien.
- **Funciones pequeñas**: más fáciles de entender, probar y reutilizar.
- **Evita efectos secundarios** si no son necesarios (modificar variables globales, imprimir dentro si no hace falta).
- **Usa `return` para datos**, `print` solo para interfaz/depuración.
- **Docstrings**: documenta qué hace la función, parámetros y retorno.

Ejemplo con docstring:
```python
def convertir_a_celsius(fahrenheit: float) -> float:
    """
    Convierte una temperatura de Fahrenheit a Celsius.

    Args:
        fahrenheit: Temperatura en grados Fahrenheit.

    Returns:
        Temperatura en grados Celsius.
    """
    return (fahrenheit - 32) * 5 / 9
```

- **Validación simple** cuando aplica:
```python
def dividir(a, b):
    if b == 0:
        raise ValueError("b no puede ser 0")
    return a / b
```

- **Evita duplicación**: si copias y pegas el mismo bloque 2+ veces, crea una función.
- **Prueba tus funciones** con casos normales y límites (ej.: 0, negativos, vacío, etc.).

---
**Resumen rápido:**
- `def` define funciones.
- Parámetros reciben datos.
- `return` devuelve resultados para reutilizarlos.
- Parámetros por defecto simplifican llamadas.
- Buenas prácticas = código claro, mantenible y reutilizable.