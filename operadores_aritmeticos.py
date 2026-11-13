#OPERADORES ARITMETICOS

a = 10
b = 3

#SUMA
suma = a + b
print(f"La suma de {a} y {b} es: {suma}")

#RESTA
resta = a - b
print(f"La resta de {a} y {b} es: {resta}")

# MULTIPLICACION
multiplicacion = a * b 
print(f"La multiplicación de {a} y {b} es: {multiplicacion}")

# DIVISON flotante o decimal
division = a / b
print(f"La división de {a} entre {b} es: {division}")

# DIVISION ENTERA
division = a // b
print(f"La división entera de {a} entre {b} es: {division}")

#MODULO O RESIDUO
modulo = a % b
print(f"El módulo de {a} entre {b} es: {modulo}")

#POTENCIA O EXPONENCIACION
potencia = a ** b
print(f"La potencia de {a} elevado a {b} es: {potencia}")


#PRECEDENCIA DE OPERADORES ---------------

resultado = 10 + 3 * 2
print(f"El resultado de la Operacion 10 + 3 * 2 es: {resultado}") #16

resultado_2 = (10 + 3) * 2
print(f"El resultado de la Operacion (10 + 3) * 2 es: {resultado_2}") #26

resultado_3 = 10 * 3 // 3
print(f"El resultado de la Operacion 10 * 3 // 3 es: {resultado_3}") #10

ejercicio = ((a + b) * (a - b) / (a * b)) - ((a ** b) % 3)
print(f"El resultado de la Operacion es: {ejercicio}") #2.03333


#LIBRERIAS EN PYTHON

import math

print(math.pi)
print(math.e)
print(math.sqrt(16))


import random

print(random.random()) # Numero aleatorio entre 0 y 1