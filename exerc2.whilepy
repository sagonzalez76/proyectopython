
# 2.- Realiza un programa donde el usuario piense un número entre 1 y 100 y el ordenador, 
# preguntando si es mayor o menor que otro, debe averiguarlo.
# Ten en cuenta que la mejor estrategia es preguntar cada vez por la mitad del rango disponible 
# para eliminar la mayor cantidad posible de números:

# Primero preguntaré por 50 y, así elimino a 50 de golpe, una vez ahí, 
# si es mayor, preguntaré por 75...

# Información extra: El cociente de la división 
# (o, lo que es lo mismo, el resultado entero de la división) se realiza mediante el operador "//"
# 5//2 nos dará 2.

# Sé muy cuidadoso a la hora de hacer el algoritmo y elegir las variables. 
# Ten en cuenta que los límites superior e inferior deberán cambiar a lo largo 
# de la ejecución del programa.

# Este programa puede requerir el uso de una variable booleana. Se declara como sigue:
# variable=True o, alternativamente: variable=False


# import random
# intentos = 0
# print("JUEGO DE AZAR....")
# print("Cual es tu nombre?...")
# nombre = input()
# x = random.randint(1,100)
# print("Hola " + nombre + ", Bienvenido a mi primer juego....")
# while intentos < 6:
#     intentos = intentos + 1
#     print("Adivina mi numero que se encuentra entre 1 y 100")
#     numero = input()
#     numero = int(numero)
#     if numero < x:
#         print("Tu numero es mas bajo")
#     if numero > x:
#         print("Tu numero es mas alto")
#     if numero == x:
#         break
# if numero == x:
#     print("Eres un genio....")
#     print(nombre + " lo lograste con %d intentos" % (intentos))
#     print("Nos vemos....")
# if numero != x:
#     print("Has perdido, sera en otra oportunidad...")
#     print("Has perdido, sera en otra oportunidad...")

#     print("Nos vemos")

# start=input("Piensa en un numero e intentare adivinarlo, presiona 1 para empezar el juego una vez estes listo ")
# if(start==1):

max=100
min=0
n1=50
finalizar=False
while finalizar==False:
    msg=input("Tu numero es "+ str(n1) +"? " + " Escribe ME si es menor o MA si es mayor ,o S si " +str(n1) +" es el numero elegido  ")
    if(msg=="ME"):
        max=n1
        n1=int(n1/2)
    elif(msg=="MA"):
        min=n1
        n1=int(n1+(0.5*n1))
    else:
        finalizar=True
        print("Gracias por jugar")
# else:
#     print("Fin del Juego")
        

        
