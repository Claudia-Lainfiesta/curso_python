
#!----------------DATOS COMPUESTOS------------------

#*Creando una lista (se pueden modificar)
lista = ["Claudia", "Lainfiesta", True, 1.70]

#*Creando una tupla (NO se pueden modificar)
tupla = ("Claudia", "Lainfiesta", True, 1.70)

#!--------------------------------------------------

#*Esto es valido

#? nombre_lista[posición_indice] = "Cambio de elemento"
lista[3] = "Maquina"

#*Esto no es valido
#tupla[3] = "Maquina"

#!--------------------------------------------------

#*Creando un conjunto (set) 
# Puede redefinirse o iterar, pero no cambiar.
# No puede accederse al indice, no se repiten datos iguales
conjunto = {"Claudia", "Lainfiesta", True, 1.70}
#*Esto no es valido
#print(conjunto[3])

#!--------------------------------------------------

#*Diccionario

diccionario = {
    #'clave' : "valor",
    #'key' : "value" separado por comas
    'nombre' : "Claudia Lainfiesta",
    'canal' : "Clau",
    'esta_emocionado' : True,
    'altura' : 1.70,
    'dato_duplicado' : "Clau"
}

print(diccionario['altura'])
print(lista[3])