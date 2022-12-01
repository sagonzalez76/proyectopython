edad = input("Ingrese la edad: ")
# while edad.isdigit():
while not edad.isdigit():
    edad = input("Digita un numero")
edad = int(edad)
if edad < 26:
    print("Eres estudiante")
elif edad > 25 and edad < 66:
    print("Eres profesor")
elif edad > 65:
    print("Eres Master")


# x = edad.isdigit()
# if (x==True):
#     edadn=int(edad)
#     while edadn < 26:
#         print("Eres estudiante")
#     else:
#         print("Eres profesor")
# else:
#     print("Ingrese solo numeros")
# while edadn < 26:
#   print(i)
#   if i == 3:
#     break
#   i += 1
