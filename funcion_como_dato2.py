"""
Crea una función que:
    -reciba una lista
    -reciba una función
    -reciba un número
    -aplique la función solo a los números mayores que ese número
Ejemplo:
“aplica cuadrado solo a los mayores de 10”
"""
numbers = [6,8,10,12,14,16]

def apply(numbers, func, cond):
    """
    Crea una lista que aplica un funcion en especifico
    unicamente a valores de la lista numbers que cumplan
    con la condicion de ser mayor a un determinado numero
    """
    return [func(num) for num in numbers if num > cond]

def square(num):
    """
    eleva al cuadrado un numero
    """
    return num ** 2

print(apply(numbers,square,10))
