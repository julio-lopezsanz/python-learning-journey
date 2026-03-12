"""
El ejercicio clásico de programación. 
Imprime los números del 1 al 50. 
Pero: 
    - si el número es múltiplo de 3  imprime 'Fizz' 
    - si es múltiplo de 5, imprime 'Buzz'.
    - Si es múltiplo de ambos, imprime 'FizzBuzz'
"""

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} - FizzBuzz")
    elif num % 5 == 0:
        print(f"{num} - Buzz")
    elif num % 3 == 0 :
        print(f"{num} - Fizz")
    else:
        print(num)
