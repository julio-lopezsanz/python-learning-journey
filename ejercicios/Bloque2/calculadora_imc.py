"""
Pide al usuario: 
    - Peso (kg) 
    - Altura (m). 
Calcula: 
    - IMC = peso / altura². 
Imprime 
¿Es menor a 18.5, entre 18.5 y 24.9, o mayor? 
(Solo imprime el número por ahora, los condicionales los practicarás después).
"""

weight = float(input("Ingrese su peso(kg): "))
height = float(input("Ingrese su altura(m): "))

imc = round(weight / (height**2),2)

print(f"Su IMC es: {imc}")
