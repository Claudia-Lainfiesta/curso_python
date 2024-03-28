
#!---------------VARIABLES---------------------

#? declaran = definen
nombre = "Claudia"

#*Definiendo variable con camelCase
nombreCompleto = "Claudia Herrera"

#*Definiendo variable con snake_case (recomendación para python)
nombre_completo = "Claudia Herrera"

#!---------------------------------------------

#*Concatenar con +
bienvenida = "Hola " + nombre + " Como estas?"
print(bienvenida)

#*Concatenar con F-string

bienvenida = f"Hola {nombre} Como estas?"
print(bienvenida)

#!---------------------------------------------

#*operadores de pertenencia (in / not in)

print("ola" in bienvenida) #True
print("Polo" in bienvenida) #False

print("ola" not in bienvenida) #False
print("Polo" not in bienvenida) #True

#!---------------------------------------------

#*borrar datos
del nombre