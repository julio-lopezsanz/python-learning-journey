"""
Sin usar math.factorial 
calcula el factorial de un número dado por el usuario usando un bucle. 
    - Valida que el número sea positivo y no mayor a 15. 
    - Muestra cada paso del cálculo
"""
result = 1
num = int(input("ingresa un numero: "))

if num < 0 or num > 15:
    print("ERROR: el numero no debe negativo ni mayor a 15")
else:
    for i in range(1, num + 1):
        result = result * i


print(" × ".join(str(i) for i in range(num, 0, -1)) + f" = {result}")
