"""Ejercicio 2 — Parámetros

Crea una función calcular_imc(peso, altura) que:

reciba peso en kg

reciba altura en metros

devuelva el IMC"""

# Fórmula del IMC: peso / [altura (en metros) ** 2]

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Ejemplo de uso
peso_1 = float(input("Ingresa tu peso en kg: "))
altura_1 = float(input("Ingresa tu altura en metros (ej: 1.70): "))
imc_1 = calcular_imc(peso_1, altura_1)
print(f"Tu IMC es: {imc_1:.2f}")



# Opcion mas optima:
'''def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el IMC (peso en kg / altura en m²)."""
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que 0.")
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return peso / (altura ** 2)


def pedir_float(mensaje: str) -> float:
    while True:
        try:
            texto = input(mensaje).strip().replace(",", ".")
            return float(texto)
        except ValueError:
            print("Entrada inválida. Ingresa un número (ej: 1.70 o 1,70).")


def pedir_altura_en_metros() -> float:
    """
    Pide altura en metros y valida que esté en un rango razonable.
    Evita que el usuario ingrese centímetros como 170.
    """
    while True:
        altura = pedir_float("Ingresa tu altura en metros (ej: 1.70): ")

        # Si ingresa 3 dígitos típico de centímetros (ej: 170)
        if altura >= 3:
            print("Parece que ingresaste centímetros. Debes ingresar metros (ej: 1.70).")
            continue

        # Rango razonable en metros
        if not (0.5 <= altura <= 2.5):
            print("Altura fuera de rango. Ingresa un valor en metros entre 0.50 y 2.50.")
            continue

        return altura


def pedir_peso_en_kg() -> float:
    while True:
        peso = pedir_float("Ingresa tu peso en kg: ")
        if not (1 <= peso <= 500):
            print("Peso fuera de rango. Ingresa un valor entre 1 y 500 kg.")
            continue
        return peso


def main() -> None:
    peso = pedir_peso_en_kg()
    altura = pedir_altura_en_metros()
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")


if __name__ == "__main__":
    main()"""'''