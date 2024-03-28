
#!-----------OPERADORES DE COMPARACIÓN--------------------------------

#* ==
igual_que = 5 == 6

#* !=
distinto_que = 5 != 6

#* >
mayor_que = 5 > 6

#* <
menor_que = 5 < 6

#* >=
mayor_igual = 5 >= 6

#* <=
menor_igual = 5 <= 6

#!--------------------------------

print("El resultado de igual que: ", igual_que)
print("El resultado de distinto que: ", distinto_que)
print("El resultado de mayor que: ", mayor_que)
print("El resultado de menor que: ", menor_que)
print("El resultado de mayor o igual que: ", mayor_igual)
print("El resultado de menor o igual que: ", menor_igual)

#!--------------------------------------------------------

#*Cálculos combinados
a = 5
b = 10
c = 20
comparación = a +b == c

print(a, "+", b, "==", c, "=", comparación)

#!-----------------------------------------------------------

#*Ejemplo de uso: comparación de usuarios

password_almacenada = "Claudia18"
password_escrita = "Claudia18"

print(password_almacenada == password_escrita)