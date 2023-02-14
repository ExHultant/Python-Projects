#Elabore un programa que lea 3 numeros e indique si los numeros fueron ingresados de
# de forma ascendente o no #
print('Ingrese un numero')
n1 = int(input())
print('Ingrese un numero')
n2 = int(input())
print('Ingrese un numero')
n3 = int(input())
if n2 > n1 and n3 > n2:
    print('Es Ascendente')
else:
    print('No es Ascendente')