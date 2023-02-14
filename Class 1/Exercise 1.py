#Codifique un programa que calcule
#el mayor de dos numeros, tome en cuenta que los nros pueden ser iguales#
'Condicionales'
number1 = int(input('ingrese un numero: '))
number2 = int(input("Ingrese otro numero xd: "))
if number1 == number2:
    print('Los numeros son iguales')
else:
    if number1 > number2:
        print(f'el {number1} es mayor a {number2}')
    else:
        print('el mayor es el numero ', number2)