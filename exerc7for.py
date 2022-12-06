# usuario=[]
# numeroscal=[]
# veces=int(input("Cuantos numeros desea ingresar "))
# vecesarray=[*range(veces)]

# for i in vecesarray:
#     numero=int((input("Introduzca un numero")))
#     usuario.append(numero)
#     numero=numero**2
#     numeroscal.append(numero)

# print(usuario)
# print(numeroscal)


numeros=[1,2,3]
numerosusuario=[]

for i in numeros:
    num=int(input("Introduce 3 numeros"))
    numerosusuario.append(num)
    for j in numerosusuario:
        if i==j:
            print ("Coincidencia")
            respuesta="identicos"
if (numeros==numerosusuario or numerosusuario==numeros):
    print("LOS VECTORES SON IDENTICOS")
else:
    print("LOS VECTORES SON DISTINTOS")

# lista=(1,2,3,4)
# lista1=(1,'carlos')
 
# for i in lista:
#     for j in lista1:
#         if i==j:
#             print ("coincide el valor %s" % j)