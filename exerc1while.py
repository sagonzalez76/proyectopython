# Ahora toca practicar lo aprendido con varios ejercicios que deben resolverse con lo aprendido. Se
# recomienda encarecidamente emplear tiempo en resolverlo en vez de ir a ver la solución
# directamente.

# 1.- Realiza un programa donde se pida dos números y la operación a realizar (a elegir entre suma,
# resta, multiplicación y división). Posteriormente debe dar el resultado y preguntar si queremos
# hacer otra operación. Identificar si se quiere realizar una división por 0.

# Ten en cuenta que los operadores matemáticos simples son:&quot; + &quot; para la suma,&quot; - &quot; para la resta,&quot;
# * &quot; para la multiplicación y &quot; / &quot; para la división. En este programa se recomienda convertir el texto
# que devuelve input a un número tipo float.
n1=float(input("Introduce tu primer numero "))
n2=float(input("Introduce tu segundo numero "))
o=int(input("Presiona 1 para realizar una suma, 2 para restar,3 para multiplicar y 4 para dividir "))
if(o==1):
    suma=n1+n2
    print("La suma de los numeros "+ str(n1) +" y " + str(n2) +" es " + str(suma))
elif (o==2):
    resta=n1-n2
    print("La resta de los numeros "+ str(n1) +" y " + str(n2) +" es " + str(resta))
elif (o==3):
    multiplicacion=n1*n2
    print("La multiplicacion de los numeros "+ str(n1) +" y " + str(n2) +" es " + str(multiplicacion))
elif (o==4 and n2!=0):
    division=n1/n2
    print("La division de los numeros "+ str(n1) +" y " + str(n2) +" es " + str(division))
else:
    print("No puedes dividir entre cero")
