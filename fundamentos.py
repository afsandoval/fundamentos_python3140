print("Hola Mundo")

#Tipo de Escritura de las Variables --------------

#camelCase
aprendizSena = "SENA"

#PascalCase
AprendizSena = "SENA"

#snake_case - OK
aprendiz_sena = "SENA"

#Reglas de las Variables:

nombre_completo_1 = "Andres Sandoval"


# Tipos de datos Primitivos ---------------
nombre = "Felipe"
print(type(nombre)) #str

edad = 32
print(type(edad)) #int

altura = 1.80
print(type(altura)) #float

activo = True
print(type(activo)) #bool

complejo = 2 + 3j
print(type(complejo)) #complex

byte = b"Hola"
print(type(byte)) #bytes

nulo = None
print(type(nulo)) #NoneType

# Tipos de datos Estructuras ---------------

lista = ["Python", "Javascript"]
print(type(lista)) #list

conjunto = {"Html", "Css"}
print(type(conjunto)) #set

tupla = ("Java", "C#")
print(type(tupla)) #tuple

diccionario = {"nombre": "Andres", "edad": 32}
print(type(diccionario)) #dict

rango = range(5)
print(type(rango)) #range


# Conversción de Tipos de Datos o Casteo ---------------

# Casteo: Entero -> Texto
telefono = 3214815173 #int
print(type(telefono), telefono)

telefono_str = str(telefono) #string
print(type(telefono_str), telefono_str)


#Casteo: Texto -> Entero
cedula = "105233213" #string
print(type(cedula), cedula)

cedula_int = int(cedula) #entero
print(type(cedula_int), cedula_int)


#Casteo: Booleano -> Entero
matriculado = False
print(type(matriculado), matriculado) #bool

matriculado_int = int(matriculado)
print(type(matriculado_int), matriculado_int) #entero

#Casteo: Entero -> Booleano
activo = 1
print(type(activo), activo) #int

activo_bool = bool(activo)
print(type(activo_bool), activo_bool) #bool

#Casteo: Decimal -> Entero
promedio = 4.13
print(type(promedio), promedio) #float

promedio_int = int(promedio)
print(type(promedio_int), promedio_int)# entero

#Casteo: Entero -> Decimal
edad = 32
print(type(edad), edad) #int

edad_float = float(edad)
print(type(edad_float), edad_float) #float

#Casteo: Booleano -> Decimal

beneficio = True
print(type(beneficio), beneficio) #bool

beneficio_float = float(beneficio)
print(type(beneficio_float), beneficio_float) #float

#Casteo: Decimal -> Booleano
descuento = 10.5
print(type(descuento), descuento) #float

descuento_bool = bool(descuento)
print(type(descuento_bool), descuento_bool) #bool


# Este es un Comentario de una sola línea

"""" Este es un comentario de varias lineas
que se utiliza para explicar el código de manera más detallada """


# Indentacion en Python

#Condicional if

if 5 > 2:
    print("5 es Mayor que 2")
else:
    print("5 no es Mayor que 2")
    

#INPUT : Entrada de datos
nombre_completo = input("Ingrese tu nombre completo: ")
programa = input("Cual es tu programa de Formacion ? ")

#OUTPUT : Salida de datos
print("Hola " + nombre_completo + " Bienvenido al curso de Python")
print("Hola", nombre_completo, "Bienvenido al curso de Python")

print("Hola mi nombres es:", nombre_completo, "y estoy en el programa de: ", programa)

#Impresion con Formato F-String - OK
print(f"Hola mi nombres es {nombre_completo}, y estoy en el Programa de: {programa}")

