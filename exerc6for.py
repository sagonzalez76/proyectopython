usuario=[]
numeroscal=[]
veces=int(input("Cuantos numeros desea ingresar "))
vecesarray=[*range(veces)]

for i in vecesarray:
    numero=int((input("Introduzca un numero")))
    usuario.append(numero)
    numero=numero**2
    numeroscal.append(numero)

print(usuario)
print(numeroscal)