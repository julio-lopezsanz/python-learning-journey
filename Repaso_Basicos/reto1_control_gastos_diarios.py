"""
Estás llevando el control de tus gastos diarios.
El programa debe pedir al usuario: 
    - gastos 
    - calcular el total
    - el promedio 
    - decir si el usuario se pasó de un presupuesto diario.

El programa termina cuando el usuario escriba 0.
"""
budget = 500.0
expenses = []

while True:
    try:
        expen = float(input("\nIngresa tus gastos de hoy (0 para terminar): "))
    except ValueError:
        print("Error: solo se permiten números.")
        continue

    if expen == 0:
        print("\nRealizando cálculos...")
        break

    if expen < 0:
        print("El gasto no puede ser negativo.")
        continue

    expenses.append(expen)

if not expenses:
    print("\nNo hay datos disponibles para realizar cálculos.")
else:
    total = sum(expenses)
    average = round(total / len(expenses), 2)

    print("\n========= Datos finales =========")
    print(f"Gastos totales: {total}")
    print(f"Promedio de gastos: {average}")

    if total > budget:
        print(f"Te pasaste del presupuesto por: {total - budget}")
    else:
        print(f"Presupuesto restante: {budget - total}")
