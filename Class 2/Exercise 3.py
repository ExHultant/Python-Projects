#Elabore un programa que lea la fecha de ingreso de un empleado y muestre la antiguedad del
# trabajador #
print('Ingrese su nombre y apellido')
name = str(input())
print('Ingrese su dia de ingreso')
dia_ingr = int(input())
print('Ingrese su mes de ingreso')
mes_ingr = int(input())
print('Ingrese su año de ingreso')
ano_ingr = int(input())
print('Ingrese el dia presente')
dia = int(input())
print('Ingrese el mes actual')
mes = int(input())
print('Ingrese el año vigente')
ano = int(input())
anti1 = ano - ano_ingr - 1
anti2 = mes - mes_ingr + 12
anti3 = dia - dia_ingr + 30
print(f'Trabajador: {name} \n Fecha de Ingreso: {dia_ingr} / {mes_ingr} / {ano_ingr} \n Antigüedad: {anti1} años {anti2} meses  y {anti3} dias')
