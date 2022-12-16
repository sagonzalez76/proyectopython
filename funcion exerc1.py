# CALCULAR CUANTOS SEGUNDOS TIENE UNA MEDIDA DE TIEMPO.

# def tiemposeg():
#     hr = int(input("Introduzca las horas "))
#     min = int(input("Introduzca los minutos "))
#     sg = int(input("Introduzca los segundos "))

#     total = (hr * 3600) + (min * 60) + sg
#     print("Los segundos totales son ", total)


# tiemposeg()

# ESCRIBIR UNA FUNCION QUE RECIBE COMO PARAMETRO UNA
# FRASE ESTABLECIDA Y LA REPITA UN N NUMERO DE VECES

# frase = input("Introduzca una frase: ")


# def frases(frase):
#     veces = int(input("Cuantas veces desea repetirla? "))
#     while veces > 0:
#         print(frase)
#         veces = veces - 1


# frases(frase)

# CALCULAR CUANTOS MINUTOS TIENE UNA MEDIDA DE TIEMPO.

# def tiempomin():
#     hr = float(input("Introduzca las horas "))
#     min = float(input("Introduzca los minutos "))
#     sg = float(input("Introduzca los segundos "))

#     total = (hr * 60) + min + (sg/60)
#     print("Los minutos totales son ", total)

# tiempomin()


# CALCULAR CUANTAS HORAS TIENEN 2'000.360
# seg y a su vez cuantos minutos
# tiempo=2000360
# def tiempohr(tiempo):

#    hr=tiempo/3600
#    min=tiempo/60
#    print("Las horas totales son ", hr)
#    print("Los minutos totales son ", min)

# tiempohr(tiempo)


# n1=int(input("Introduzca el primer numero "))
# n2=int(input("Introduzca el segundo numero "))

# def pares (n1, n2):
#     while n1 <= n2:
#         if n1%2==0:
#             print(n1)
#         else:
#             ()

#         n1+=1

# pares(n1, n2)


def domino():
    contador=0
    contadorv=[]
    for i in range(1, 7):
        for j in range(1, 7):
            if j!=contador:
                print(i, "/", j)
                # print("\n") 
            else:
                ()
        contadorv.append(contador)
        print("A es ", contador)
        contador += 1
domino()


# animales=["gato","perro"]
# animalesvacio=[]
# for i in animales:
#     for j in i:
#         animalesvacio.extend(j)
# print(animalesvacio)


# escribir una funcion que imprima por panatalla
# todas las dichas del domino de una por linea y sin repeti
