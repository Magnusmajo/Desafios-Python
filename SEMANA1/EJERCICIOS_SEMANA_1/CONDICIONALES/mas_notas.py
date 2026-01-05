"""≥ 9 → “Excelente”

≥ 6 → “Aprobado”

< 6 → “Reprobado”"""

while True:
    try:
        nota = float(input("Ingrese una nota: "))
        
        if nota >= 9:
            print("Excelente!")
        elif nota >= 6:
            print("Por los pelo, Aprobado")
        else:
            print("Suspenso, estudia mas!")
        break
    
    except ValueError:
        print("Ingresa un numero valido")