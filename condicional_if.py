# CONDICIONALES IF/ELIF/ELSE

#Estructura del Condicional IF:

if True:
    print("Se ejecuta la Instruccion")
    
#Ejemplo del IF - ELSE

edad = 12

if edad > 18:
    print("Eres un Adulto")
else:
    print("Eres Joven")
    

#Estructura del ELIF:
if False:
    print("La primera condicion")
elif True:
    print("Segunda condicion")
elif True:
    print("Tercera condicion")
else:
    print("Todas las condiciones son False")
    
#EJERCICIO: CLASIFICACION DE EDAD

edad = 100

if edad < 18: #False
    print("Eres menor de Edad")
elif edad >= 18 and edad < 65: #False
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
    

#ESTRUCTURA CONDICIONAL ANIDADA

if True:
    if False:
        print("Se ejecuta la instruccion")
    elif True:
        print("Se ejecuta la instruccion")
    else:
        print("No se ejecuta la instruccion")
else:
    print("No se ejecuta la instruccion")
    

# Ejercicio: Clasificacion de Edad IF anidado

edad = 80

if edad < 18:
    if edad > 12 and edad < 18:
        print("Adolescente")
    else:
        print("Niño")
else:
    if edad >= 18 and edad < 60:
        print("Adulto")
    else:
        print("Adulto Mayor")
        
#EJERCICIO PARTIDO CON IF:

marcador_colombia = int(input("Ingrese el Marcador de Colombia: "))
marcador_chile = int(input("Ingrese el Marcador de Chile: "))

if marcador_colombia > marcador_chile:
    print("Colombia es el Ganador del Partido :D ")
elif marcador_colombia == marcador_chile:
    print("Quedamos Empatados")
else:
    print("Perdimos el Partido :( ")
    
    
# OPERADOR TERNARIO:

numero = 4

if numero % 2 == 0:
    print("El numero es Par")
else:
    print("El numero es Impar")
    
print("El numero es Par" if numero % 2 == 0 else "El numero es Impar")