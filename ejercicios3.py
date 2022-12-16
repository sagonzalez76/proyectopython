# Elabora un programa que muestre una lista de números la cual
# pida al usuario desde que numero quiere y hasta que numero
# quiere mostrar por ejemplo si  ingresa  2  y 10  debería mostrar
# 2,3,4,5,6,7,8,9,10 o si  ingresa  2  y -10  debería mostrar
# 2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10


# n1=int(input("Introduce el primer numero"))
# n2=int(input("Introduce el segundo numero"))
# x=0
# if (n1>0 and n2>0):
#     x=1
# elif (n1>0 and n2<0):
#     x=-1
# elif (n1<0 and n2>0):
#     x=1
# else:
#     x=1

# for i in range(n1,n2,x):
#     print(i)

###########################################################################################################


# Realiza un programa que muestre los numeros pares desde un
# numero predeterminado hasta otro numero predeterminado

# n1=int(input("Introduce el primer numero"))
# n2=int(input("Introduce el segundo numero"))
# x=0
# if (n1>0 and n2>0):
#     x=1
# elif (n1>0 and n2<0):
#     x=-1
# elif (n1<0 and n2>0):
#     x=1
# else:
#     x=1

# for i in range(n1,n2,x):
#     if i%2==0:
#         print(i)


###########################################################################################################

# Realiza un programa que muestre los numeros impares desde un
# numero predeterminado hasta otro numero predeterminado


# n1=int(input("Introduce el primer numero"))
# n2=int(input("Introduce el segundo numero"))
# x=0
# if (n1>0 and n2>0):
#     x=1
# elif (n1>0 and n2<0):
#     x=-1
# elif (n1<0 and n2>0):
#     x=1
# else:
#     x=1

# for i in range(n1,n2,x):
#     if i%2==1:
#         print(i)

###########################################################################################################

# Calcular el factorial de un numero ingresado  por teclado, si el
# factorial de un numero  se  representa de la siguiente forma n! =
# 1*2*3*4*5......(n-1)*n    Ejemplo 2: 4! = 1*2*3*4  = 24; tenga en
# cuenta que el  factorial de 0! es 1   0! = 1


# n1=int(input("Introduce el factorial "))
# fact = 1
# for i in range(1,n1+1):
#     fact= fact * i

# print(fact)


###########################################################################################################

# Realiza un programa que imprima una secuencia de numeros de
# uno en uno desde el que el usuario desee, el programa debe
# pedirle al usuario después de que imprima un numero en pantalla
# le pregunte si desea continuar o no mostrando en pantalla

# 1-10

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 1- DESEA CONTINUAR-SI
# 2-DESEA CONTINUAR-SI
# 3-DESEA CONTINUAR-NO
# FIN

# n1=int(input("Introduce el primer numero "))
# n2=int(input("Introduce el segundo numero "))

# x=0
# if (n1>0 and n2>0):
#     x=1
# elif (n1>0 and n2<0):
#     x=-1
# elif (n1<0 and n2>0):
#     x=1
# else:
#     x=1

# for i in range(n1,n2+x):
#         print(i)
#         print("Desea continuar? Presione s")
#         a=input()
#         if (a!='s') and (a!='S'):
#             print('FIN DEL CICLO')
#             break


# Escribir una aplicación que reciba un número entero k e imprima
# su descomposición en factores primos.

n1 = int(input("Introduce un numero "))
primos = []

for i in range(2, n1 + 1):
    while n1 % i == 0:
        primos.append(i)
        n1 = n1 / i
print(primos)
