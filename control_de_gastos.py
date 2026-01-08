"""
Contexto real: registro básico de gastos personales.

Objetivo:
Dada una lista de números gastos = [120, 50, 300, 90, 200]:
- Calcula el gasto total
- Calcula el gasto promedio
- Devuelve una nueva lista solo con los gastos mayores al promedio
"""
expenses = [120, 50, 300, 90, 200]

#Recordatorio: los nombres de las funciones deben ser discriptivas a lo que retornan
def above_average_expenses(expenses):
    """
    Calcula el gasto total, del que saca el gasto promedio
    y devuelve una lista con los gastos mayores al promedio
    """
    #Retorna lista vacia, ya que la funcion retorna una lista
    #Si devolviera un string u otra cosa, a futuro causaria problemas
    #Esto cambia cuando se ve el tema de "excepciones"
    if not expenses:
        return []

    #Suma todos los elementos de la lista de gastos
    total_expenses = sum(expenses)

    #Saca el promedio de la suma previamente calculada
    average_expenses = total_expenses / len(expenses)

    #Crea una lista con los elementos de los gastos que son mayor al promedio
    result = [expense for expense in expenses if expense > average_expenses]

    return result

print(above_average_expenses(expenses))
