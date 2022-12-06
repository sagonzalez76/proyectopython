# 3.- Realiza un programa donde se le pidan números al usuario hasta que introduzca 3 impares. Si
# son pares, seguirá pidiendo indefinidamente. Cada vez que se introduce un impar, el programa nos
# dice cuántas oportunidades nos quedan antes de terminar salvo al llegar a la tercera vez, debe
# decir que se termina el programa.

# En este caso, diferenciar si es par o impar lo podemos hacer con la operación que nos da el resto
# de una división. Su sintaxis es: %

# 4 % 2 = 0

# 5 % 2 = 1

# Se le llama módulo. Nada que ver con el módulo de un vector en matemáticas.

intentos=3
while intentos!=0:
    n1=int(input("Introduce un numero par "))
    if n1%2==1:
        intentos=intentos-1
        if intentos !=0:
            print("Te quedan " + str(intentos) + " intentos")
        else:
            print("Se termina el juego")


