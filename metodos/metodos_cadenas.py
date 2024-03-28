
#!----------------MÉTODOS EN CADENAS---------------------------

cadena1 = "Hola soy Claudia"
cadena2 = "123456789"
cadena3 = "abcdefghijklmnopqrstuvwxyz"
cadena4 = "Bienvenido crack"

#?Función principal
#*DIR --> es una función para saber que puede hacer la variable
print(dir(cadena1))

#*****************************************************************
#?Métodos
#*Estructura
#*variable = dato.método(parámetros_opcionales)

#*----------------------------------------------------------------
#?Métodos que convierten

#*Upper: cambia todo el texto a mayúsculas
resultado_upper = cadena1.upper()
print(resultado_upper)

#*Lower: cambia todo el texto a minúscula
resultado_lower = cadena1.lower()
print(resultado_lower)

#*Capitalize: primer letra en mayúscula
resultado_capitalize = cadena1.capitalize()
print(resultado_capitalize)

#*----------------------------------------------------------------
#?Métodos que realizan una búsqueda

#*Find: búsqueda de una cadena en otra cadena, si no hay coincidencias devuelve -1

resultado_find = cadena1.find("d")
print(resultado_find)

#*Index: búsqueda de una cadena en otra cadena, si no hay coincidencias devuelve una excepción (error)

resultado_index = cadena1.index("d")
print(resultado_index)
#*----------------------------------------------------------------
#?Métodos que consultan

#*Isnumeric: si es numérico, devuelve TRUE, de lo contrario FALSE

resultado_isnumeric = cadena2.isnumeric()
print(resultado_isnumeric)


#*Isalpha: si es alfanumérico (solo de la A a la Z), devuelve TRUE, de lo contrario FALSE

resultado_isalpha = cadena3.isalpha()
print(resultado_isalpha)

#*----------------------------------------------------------------
#?Métodos que realizan una búsqueda

#*Count: búsqueda en un cadena de otra cadena, devuelve la cantidad de coincidencias

resultado_count = cadena1.count("a")
print(resultado_count)

#*----------------------------------------------------------------
#?Función que realiza una búsqueda

#*Len: cuenta la cantidad de caracteres que tiene una cadena
resultado_len = len(cadena1)
print(resultado_len)

#*----------------------------------------------------------------
#?Métodos que verifican

#*Startswith: verificación de una cadena si empieza con otra cadena dada, si es así devuelve TRUE, de lo contrario devuelve FALSE

resultado_startswith = cadena1.startswith("Hola")
print(resultado_startswith)

#*Endswith: verificación de una cadena si termina con otra cadena dada, si es así devuelve TRUE, de lo contrario devuelve FALSE

resultado_endswith = cadena1.endswith("Claudia")
print(resultado_endswith)
#*2:07