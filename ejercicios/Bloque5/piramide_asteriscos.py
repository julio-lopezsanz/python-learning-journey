"""
Pide al usuario la altura de la pirámide. 
Dibuja una pirámide centrada. 
Para altura 4:     
   *    
  ***   
 *****  
*******
"""

num = int(input("Ingresa la altura que tendra la piramide: "))

for i in range(num):
    print(" " * (num - i -1) + "*" * (2 * i + 1))
