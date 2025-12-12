# Condicionales y Flujo de Decisión

<img width="438" height="379" alt="Image" src="https://github.com/user-attachments/assets/75f9f0ea-7e19-4f33-8336-e678973d8fae" />

## Teoría esencial
Los condicionales permiten que un programa tome decisiones comparando valores y ejecutando bloques de código diferentes según el resultado de esas comparaciones. En Python, la estructura básica utiliza palabras clave como `if`, `elif` y `else`, y se apoya en operadores relacionales y lógicos para evaluar condiciones.

### 🔹 1. Estructura básica
```python
if condicion_principal:
    # bloque ejecutado si la condición es verdadera
elif condicion_alternativa:
    # bloque ejecutado si la condición alternativa es verdadera
else:
    # bloque ejecutado si ninguna condición es verdadera
```
* Cada condición se evalúa de arriba hacia abajo.
* El bloque `else` es opcional, pero útil para cubrir escenarios no contemplados en las condiciones anteriores.
* La indentación (cuatro espacios por nivel) determina los bloques de código asociados a cada condición.

### 🔹 2. Reglas mentales importantes
* Piense siempre en las condiciones como preguntas que deben responderse con `True` o `False`.
* Simplifique expresiones complejas dividiéndolas en pasos intermedios o almacenando resultados en variables auxiliares.
* Recuerde que las condiciones se evalúan de manera secuencial (de arriba hacia abajo): una vez que una condición es verdadera, el resto se omite.
* Valide constantemente los límites y casos extremos (por ejemplo, valores negativos, cero o cadenas vacías).
* No necesitas elif si solo hay dos caminos, if + else basta.

### 🔹 3. Operadores clave
* **Relacionales**: `==`, `!=`, `<`, `>`, `<=`, `>=`.
* **Lógicos**: `and`, `or`, `not`.
* **Membresía**: `in`, `not in`.
* **Identidad**: `is`, `is not`.
Estos operadores permiten comparar valores numéricos, cadenas, listas y otros tipos de datos, facilitando la construcción de expresiones condicionales robustas.

### 🔹 5. Ejemplo aplicado en salud
```python
edad = 68
presion_sistolica = 150
presion_diastolica = 95

if edad >= 65 and (presion_sistolica >= 140 or presion_diastolica >= 90):
    print("Riesgo alto: programar consulta prioritaria.")
elif edad >= 40 and (presion_sistolica >= 130 or presion_diastolica >= 85):
    print("Riesgo moderado: recomendar seguimiento mensual.")
else:
    print("Riesgo bajo: mantener controles rutinarios.")
```
* Se evalúa primero si el paciente es mayor o igual a 65 años y presenta hipertensión; de cumplirse, se recomienda atención prioritaria.
* Si no, se revisa un segundo criterio para pacientes de mediana edad con presión elevada, sugiriendo seguimiento.
* En ausencia de condiciones críticas, se considera un riesgo bajo y se sugieren controles regulares.