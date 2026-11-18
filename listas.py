#LISTAS 

#Estructura de una Lista

lista = ["dato_1","dato_2","dato_3"]
print(type(lista)) # <class 'list'>

# Lista Mixta
lista_mixta = ["Hola", 123, 3.14, True, ["ADSO", "SST"]]

# LISTA DE APRENDICES SENA ADSO 3233140

# Indice:        0           1         2        3         4
aprendices = ["Miguel", "Sebastian","Lizeth", "Oscar", "Elkin"]
print(aprendices)

#Acceder a un Elemento de la Lista
print(aprendices[2]) # Lizeth

#Modificar a un Elemento de la Lista
aprendices[0]= "Luis"
print(aprendices)

#Consultar Rangos de Elementos en las Lista
print(aprendices[0:3]) #['Luis', 'Sebastian', 'Lizeth']
print(aprendices[2:4]) #['Lizeth', 'Oscar']
print(aprendices[0::2]) #['Luis', 'Lizeth', 'Elkin']

#CONCATENAR LISTAS +
programas_tecnicos = ["Sistemas Teleinformaticos","Redes"]
programas_tecnologo = ["ADSO", "Topografia"]

programas_SENA = programas_tecnicos + programas_tecnologo
print(programas_SENA) # ['Sistemas Teleinformaticos', 'Redes', 'ADSO', 'Topografia']

# EXTENDER LISTAS .extend()
nuevos_programas_tecnicos = ["Inteligencia Artificial", "Mineria de Datos", "Redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos) #['Sistemas Teleinformaticos', 'Redes', 'Inteligencia Artificial','Mineria de Datos']

# MEDIR LA LONGITUD DE UNA LISTA .len()
print(len(programas_tecnicos)) # 5
print(len(programas_tecnologo)) # 2

#CONTAR ELEMENTOS REPETIDOS EN UNA LISTA .count()
print(programas_tecnicos)
print(programas_tecnicos.count("Redes")) #2

#OBTENER EL INDICE DE UN ELEMENTO .index()
print(aprendices.index("Lizeth")) # [2]
print(programas_tecnicos.index("Mineria de Datos")) # [3]
print(programas_tecnologo.index("ADSO")) # [0]

#COPIAR UNA LISTA NUEVA .copy()
nueva_lista_aprendices = aprendices.copy()
print(nueva_lista_aprendices)

#AGREGAR NUEVOS ELEMENTOS con .append() al Final de la Lista
nueva_lista_aprendices.append("Adriana")
nueva_lista_aprendices.append("Diana")
print(nueva_lista_aprendices)

#AGREGAR UN NUEVO ELEMENTO EN UNA POSICION DEL INDICE .insert()
nueva_lista_aprendices.insert(1, "Dayana")
print(nueva_lista_aprendices)

#ELIMINAR UN ELEMENTO DE LA LISTA

# .remove() Elimina la primera ocurrencia de la Lista
nueva_lista_aprendices.remove("Oscar")
print(nueva_lista_aprendices)

# .pop() Elimina el Elemento segun su Indice []
nueva_lista_aprendices.pop(0)
print(nueva_lista_aprendices)

# .clear() Limpia todos los Elementos de la Lista
# nueva_lista_aprendices.clear()
# print(nueva_lista_aprendices)

# ORDENAR LAS LISTAS:

# Ordenar Ascendentemente A-Z .sort()
nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

#Ordenar Descendentemente Z-A .reverse()
nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)

# BUSCAR ELEMENTOS EN LA LISTA CON EL OPERADOR "IN"
if "Diana" in nueva_lista_aprendices:
    print("Diana se encontro en la Lista de Aprendices")
else:
    print("Diana NO se encontro en la Lista de Aprendices")
    
busqueda = "Diana" in nueva_lista_aprendices
print(busqueda) #True


