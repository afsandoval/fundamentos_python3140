# CONJUNTOS - SETS

#Estructura de un Conjunto

conjunto = {"elemento_1", "elemento_2", "elemento_3"}
print(type(conjunto)) # <class 'set'>

#Declarar un Conjunto vacio
conjunto_2 = set()
print(type(conjunto_2)) #<class 'set'>

conjunto_3 = {}
print(type(conjunto_3)) #<class 'dict'>

# Crear un Conjunto (No permite elementos Duplicados)
programas = {"ADSO", "SST", "Mineria", "ADSO", "SST"}
print(programas) # {'Mineria', 'SST', 'ADSO'}

#METODOS DE LOS CONJUNTOS

frutas = {"mango", "guayaba", "mora", "manzana", "mandarina"}

#Agregar un nuevo Elemento a el Conjunto
frutas.add("fresas")
print(frutas) # {'mora', 'fresas', 'mango', 'guayaba'}

frutas.add("mora") # Elemento Duplicado
print(frutas)

#Eliminar un Elemento del Conjunto

# Metodo .remove()
frutas.remove("mango")
print(frutas)

# frutas.remove("pera") # Lanza KeyError si no existe
# print(frutas)

# Metodo .discard()
frutas.discard("mora")
print(frutas)

frutas.discard("pera")
print(frutas)

#Metodo .pop() Eiminacion Aleatoria
elemento = frutas.pop()
print(elemento)
print(frutas)

# Metodo .clear() Limpia todos los Elementos
frutas.clear()
print(frutas) # set()

# Eliminar todo el Conjunto con el Metodo "del"
# del frutas
# print(frutas) # NameError: name 'frutas' is not defined

#Verificar la Pertenecia de un Elemento en un Conjunto: Busqueda
aprendices = {"felipe", "andres", "pepito"}

print("felipe" in aprendices) #True
print("juan" in aprendices) #False


#OPERACIONES DE LA TEORIA DE CONJUNTOS

aprendices_formacion = {"jennifer", "lizeth", "diana", "alejandra","adriana"}
aprendices_apoyo = {"diana", "adriana", "luis", "sebastian", "oscar"}

# UNION: Extrae todos los elementos de los dos Conjuntos

#Operador UNION "|"
union_aprendices = aprendices_formacion | aprendices_apoyo 
print(union_aprendices)

# Metodo UNION()
union_aprendices_2 = aprendices_formacion.union(aprendices_apoyo)
print(union_aprendices_2)

# {'oscar', 'alejandra', 'adriana', 'jennifer', 'diana', 'luis', 'lizeth', 'sebastian'}


# INTERSECCION: Extrae los elementos que se repiten en los dos Conjuntos

# Operador INTERSECCION "&"
interseccion_aprendices = aprendices_formacion & aprendices_apoyo
print(interseccion_aprendices) # {'diana', 'adriana'}

# Metodo INTERSECCION()
interseccion_aprendices_2 = aprendices_formacion.intersection(aprendices_apoyo)
print(interseccion_aprendices_2) # {'diana', 'adriana'}

# DIFERENCIA: Extrae los elementos que no se repiten en los dos Conjuntos

# Operador DIFERENCIA "-"
diferencia_aprendices = aprendices_formacion - aprendices_apoyo
print(diferencia_aprendices) # {'jennifer', 'alejandra', 'lizeth'}

# Metodo DIFERENCIA()
diferencia_aprendices_2 = aprendices_formacion.difference(aprendices_apoyo)
print(diferencia_aprendices_2) # {'jennifer', 'alejandra', 'lizeth'}

# DIFERENCIA SIMETRICA: Extrae los elementos que no se repiten en los dos Conjuntos

# Operador DIFERENCIA SIMETRICA "^"
diferencia_simetrica_aprendices = aprendices_formacion ^ aprendices_apoyo
print(diferencia_simetrica_aprendices) # {'jennifer', 'alejandra', 'lizeth', 'luis', 'sebastian', 'oscar'}

# Metodo DIFERENCIA SIMETRICA()
diferencia_simetrica_aprendices_2 = aprendices_formacion.symmetric_difference(aprendices_apoyo)
print(diferencia_simetrica_aprendices_2) # {'jennifer', 'alejandra', 'lizeth', 'luis', 'sebastian', 'oscar'}