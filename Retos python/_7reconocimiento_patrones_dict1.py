"""
Devuelve solo los que aparezcan 3 o más veces.
"""

nums = [1,2,2,3,4,4,4,5,6,6,6,6]

#Nota: es importante en estos casos Parametrizar el límite
#ya que en codigo real tenemos que tener en cuenta que puede llegar a crecer
#por ello debemos hacer el codigo lo mas flexible a la hora de escribirlo
#en este caso, permitiendo pasar un limite minimo de manera estatica (>=3)
#puedes parametrizar, haciendolo mas flexible y con oportunidad de crecer
#(min_times)
def frequent_numbers(numbers, min_times):
    """
    Cuenta la cantidad de veces que se repite un numero en una lista y los
    almacena en un diccionario. Despues retorna unicamente los numeros que
    se repitieron mas o igual de 3 veces
    """
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return {n: v for n, v in counts.items() if v >= min_times}

print(frequent_numbers(nums,3))
