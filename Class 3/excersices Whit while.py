#Elabore un programa que calcule el sueldo de un docente.
#el valor de la hora depende de la categoria:
#CATEGORIAS:
#INSTRUCTOR = 5.20
#ASISTENTE = 5.30
#AGREGADO = 5.50
#ASOCIADO = 7.20
#TITULAR = 7.50
# SUELDO BASICO:
# SB = NHSEM/5*VALOR_HORA*30#
x = True
while x:
    print('Buen dia ingrese su categoria de docente agregada al sistema')
    NHSEM = int(input('Ingrese el numero de horas trabajadas: '))
    cate = int(input('CATEGORIAS: 1.INSTRUCTOR 2.ASISTENTE 3.AGREGADO 4.ASOCIADO 5.TITULAR: '))
    match cate:
        case 1:
            SB = ((NHSEM/5)*5.20)*30
            print(f'Usted ha seleccionado INSTRUCTOR lo que tiene un sueldo Basico de {SB}')
            break
        case 2:
            SB = ((NHSEM / 5) * 5.30) * 30
            print(f'Usted ha seleccionado ASISTENTE lo que tiene un sueldo Basico de {SB}')
            break
        case 3:
            SB = NHSEM / 5 * 5.50 * 30
            print(f'Usted ha seleccionado AGREGADO lo que tiene un sueldo Basico de {SB}')
            break
        case 4:
            SB = NHSEM / 5 * 7.20 * 30
            print(f'Usted ha seleccionado ASOCIADO lo que tiene un sueldo Basico de {SB}')
            break
        case 5:
            SB = NHSEM / 5 * 7.50 * 30
            print(f'Usted ha seleccionado TITULAR lo que tiene un sueldo Basico de {SB}')
            break
        case other:
            print('Ingrese un numero valido')