
#!----------OPERADORES ARITMÉTICOS----------

#*Suma (+) y resta (-)
suma = 12 + 5
resta = 13 - 5

#*Multiplicación (*) y división (/)
multiplicación = 12 * 5
división = 12 / 5 #Devuelve dato float (flotante)

#*potenciación (exponente -> **)
exponente = 12**5

#*División baja (//)
división_baja = 12 // 5 #devuelve dato int redondeado hacia abajo

#*Resto o módulo
resto = 12 % 5

#!---------------------------------------------------------

print("Resultado de suma: ", suma)
print("Resultado de resta: ", resta)
print("Resultado de multiplicación: ", multiplicación)
print("Resultado de división: ", división)
print("Resultado de potenciación: ", exponente)
print("Resultado de división baja: ", división_baja)
print("Resultado de resto: ", resto)

#!---------------------------------------------------------

#*Type(dato) devuelve tipo de dato de la variable
tipo_de_dato = type(división)

print(tipo_de_dato)