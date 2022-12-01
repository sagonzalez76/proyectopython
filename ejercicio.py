edad = int(input("Ingrese la edad: "))

if edad < 26:
    print("Eres estudiante")
elif edad > 25 and edad < 66:
    print("Eres profesor")
elif edad > 65:
    print("Eres Master")