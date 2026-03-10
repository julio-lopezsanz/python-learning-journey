"""
Retoma el ejercicio del IMC. 
Ahora agrega condicionales para mostrar la categoría: 
    - Bajo peso (<18.5) 
    - Normal (18.5-24.9) 
    - Sobrepeso (25-29.9)
    - Obesidad (30+). 
Valida que peso y altura sean valores positivos.
"""

weight = float(input("Ingrese su peso(kg): "))
height = float(input("Ingrese su altura(m): "))

if weight < 0 or height < 0:
    print("Error: La altura y el peso deben ser valores positivos")
else:
    imc = round(weight / (height**2),2)
    if imc <= 18.5:
        print(f"Su IMC es: {imc} - Bajo peso")
    elif imc <= 24.9:
        print(f"Su IMC es: {imc} - normal")
    elif imc <= 29.9:
        print(f"Su IMC es: {imc} - Sobrepeso")
    elif imc >= 30:
        print(f"Su IMC es: {imc} - Obesidad")
