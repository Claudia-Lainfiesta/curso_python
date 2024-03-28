
#!----------------CONDICIONAL IF & ELSE---------------------------

#*Estructura
"""
    If condición:
        acción

    if True:
        acción se ejecuta

    if False:
        acción NO se ejecuta
"""

#*Ejemplo No. 1
print("EJEMPLO NO. 1")
edad = 18
if edad >= 18:
    print("Puedes pasar.")
    print("Forma parte del IF.")
else:
    print("No puedes pasar.")
    print("Forma parte del ELSE.")

print("No forma parte de ninguna condición.")
print("------------------------------------")

#*Ejemplo No. 2
print("EJEMPLO NO. 2")
password_almacenada = "Claudia18"
password_escrita = "Claudia18"

if password_almacenada == password_escrita:
    print("INICIANDO SESIÓN...")
else:
    print("Contraseña errónea, intente de nuevo.")
print("-----------------------------------------")
