"""
Estás llevando el control de tus gastos diarios.
El programa debe pedir al usuario: 
    - gastos 
    - calcular el total
    - el promedio 
    - decir si el usuario se pasó de un presupuesto diario.

El programa termina cuando el usuario escriba 0.
"""
BUDGET = 500

def expenses_per_day():
    """Hace un registro de los gastos que el usuario ha realizado por día"""
    expenses = []
    while True:
        try:
            exp = float(input("Ingresa el gasto de hoy (0 para terminar): "))
        except ValueError:
            print("Error: solo números")
            continue

        if exp == 0:
            return expenses
        if exp < 0:
            print("El gasto no puede ser negativo")
            continue

        expenses.append(exp)

def total_expenses(expenses):
    """Suma los gastos registrados"""
    return sum(expenses)

def avg_expenses(expenses):
    """Saca el promedio de los gastos registrados"""
    return round(sum(expenses) / len(expenses), 2) if expenses else 0


expenses_log = expenses_per_day()

if not expenses_log:
    print("\nNo ha registrado ningún gasto. No se pueden hacer cálculos")
else:
    total = total_expenses(expenses_log)
    average = avg_expenses(expenses_log)

    print("\n---------- Registro de gasto por día ----------")
    print(f"\nGastos totales: {total}")
    print(f"\nPromedio de gastos: {average}")

    if BUDGET < total:
        print(f"\nSe ha pasado del presupuesto por: {total - BUDGET}")
    else:
        print(f"\nPresupuesto restante: {BUDGET - total}")
