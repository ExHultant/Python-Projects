'while condition'
"Inicio de condicion While"

"Inicio de contador"
number = 0
while x:
    number1 = int(input('Buenos dias, Ingrese un numero: '))
    number += 1
    x=int(input('¿Otro mas? 1.Si 2.No ... '))
    if x != 1:
        break
print(f'La cantidad de personas registradas son {number} personas')

'Match Condicion'
incremento = 1000
print(f'Usted tiene en su cuenta {incremento}')
print('¿Que desea hacer? \n 1.Depositar \n 2.Retirar \n 3.Consultar')
x = int(input())
match x:
    case 1:
        depo = int(input('Ingrese el monto a depositar: '))
        DEPO = incremento + depo
        print(f'Usted ha depsoitado: {depo}')
        print(f'Su cuenta tiene:  {DEPO}')
    case 2:
        reti = int(input('Ingrese el monto a retirar: '))
        RETI = incremento - reti
        print(f'Usted ha retirado: {reti}')
        print(f'Su cuenta tiene:  {RETI}')
    case 3:
        print(f'Usted tiene en su cuenta {incremento}')