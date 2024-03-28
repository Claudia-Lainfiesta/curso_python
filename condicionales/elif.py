
#!----------------CONDICIONAL ELSE & IF---------------------------

#*Ejemplo No. 1 --> If anidados y else if (elif)

ingreso_mensual = 72000
gasto_mensual = 8000

if ingreso_mensual > 10000:
    if ingreso_mensual- gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien con tus gastos.")
    else:
        print("No te alcanzara.")
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("Estas bien en Guatemala")
else:
    print("Eres pobre")
