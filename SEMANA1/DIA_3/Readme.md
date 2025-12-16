# Bucles (for / while) y repetición controlada

Los **bucles** permiten **repetir** un bloque de código varias veces. En Python, los más comunes son `for` y `while`. Usarlos bien implica entender **cuándo se detienen**, cómo **controlar la repetición**, y cómo **interrumpir** o **saltar** iteraciones cuando sea necesario.

---

## Teoría esencial

### ¿Qué es iterar?
**Iterar** es repetir una acción sobre una secuencia o bajo una condición.

- Si sabes **cuántas veces** (o sobre qué colección) vas a repetir, normalmente usas `for`.
- Si repites **mientras** se cumpla una condición, normalmente usas `while`.

### Errores típicos
- **Bucle infinito** (sobre todo en `while`): la condición nunca deja de cumplirse.
- Modificar una colección mientras la recorres sin cuidado.
- No entender que en Python la indentación define el bloque.

---

## Bucle `for` (el más usado)

En Python, `for` recorre elementos de un **iterable** (listas, strings, tuplas, rangos, etc.).

### Recorrer una lista
```python
nombres = ["Ana", "Luis", "Marta"]

for nombre in nombres:
    print(nombre)
```

### Recorrer un rango (repetición N veces)
```python
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
```

### `range(inicio, fin, paso)`
```python
for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)
```

### Obtener índice y valor con `enumerate`
```python
frutas = ["manzana", "pera", "uva"]

for i, fruta in enumerate(frutas):
    print(i, fruta)
```

### Recorrer dos listas a la vez con `zip`
```python
nombres = ["Ana", "Luis", "Marta"]
edades = [20, 25, 19]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

---

## Recorrer strings

Un string es un iterable: puedes recorrerlo carácter por carácter.

```python
texto = "Python"

for caracter in texto:
    print(caracter)
```

### Contar letras (ejemplo típico)
```python
texto = "banana"
contador = 0

for c in texto:
    if c == "a":
        contador += 1

print(contador)  # 3
```

### Recorrer por índice (si lo necesitas)
```python
texto = "Hola"

for i in range(len(texto)):
    print(i, texto[i])
```

---

## Bucle `while`

`while` repite mientras una condición sea `True`. Se usa cuando **no sabes de antemano** cuántas iteraciones harán falta.

### Ejemplo básico
```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

### Ejemplo con entrada del usuario (validación)
```python
edad = -1

while edad < 0:
    edad = int(input("Introduce tu edad (>= 0): "))

print("Edad válida:", edad)
```

### Evitar bucles infinitos
Asegúrate de que **algo cambia** dentro del bucle para que la condición pueda volverse `False`.

MAL (infinito):
```python
x = 0
while x < 3:
    print(x)   # x nunca cambia
```

BIEN:
```python
x = 0
while x < 3:
    print(x)
    x += 1
```

---

## `break` y `continue`

### `break` (rompe el bucle)
Sale del bucle inmediatamente, sin completar las iteraciones restantes.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# imprime 0..4
```

En `while`:
```python
i = 0
while True:
    if i == 3:
        break
    print(i)
    i += 1
```

### `continue` (salta a la siguiente iteración)
No termina el bucle, solo **salta** el resto del código de esa iteración.

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
# imprime 1, 3, 5
```

---

## Repetición controlada (buenas prácticas)

- Preferir `for` cuando recorres una colección o repites con `range`.
- Usar `while` cuando la repetición depende de una condición o evento.
- Mantener los bucles **simples** y con condiciones claras.
- Usar `break` con criterio (por ejemplo, búsqueda: “cuando lo encuentro, salgo”).
- Usar `continue` para filtrar casos sin anidar demasiados `if`.

---

## Mini-ejercicios de práctica

1) Imprime los números del 1 al 10 usando `for`.  
2) Suma los números del 1 al 100 usando `for`.  
3) Recorre un string e imprime solo las vocales.  
4) Pide una contraseña con `while` hasta que sea correcta.  
5) Recorre una lista de números e ignora los negativos usando `continue`.  
6) Busca un número en una lista y usa `break` cuando lo encuentres.