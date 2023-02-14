"""Hacer un rpograma que calcule el promedio de un estudiante nombre, cedula, 3 notas en listas"""
name = []
id = []
n1 = []
n2 = []
n3 = []
prom = []
students = 0
porcent_students = 0
alt_prom = 0
course_prom = 0
x=1
while x:
    ced = input("Ingrese cedula: ")
    id.append(ced)
    nom = input('Ingrese nombre: ')
    name.append(nom)
    not1 = int(input("Ingrese Primera nota: "))
    n1.append(not1)
    not2 = int(input("Ingrese Segunda nota: "))
    n2.append(not2)
    not3 = int(input("Ingrese Tercera nota: "))
    n3.append(not3)
    suma_notas = round(not1+not2+not3/3)
    promedio = suma_notas
    prom.append(promedio)
    print(f'Su promedio es de: {promedio}')
    students += 1
    if promedio >= 10:
        porcent_students = promedio / 100
    elif promedio >= 10:
        alt_prom = promedio * 3 / 100
    elif promedio >= 10:
        course_prom = promedio * 100 / students
    x = int(input('¿Otro estudiante? 1.Si 2.No ... '))
    if x != 1:
        break
print("Cedula".ljust(10),'Nombre'.ljust(20), 'Nota 1'.center(8), 'Nota 2'.center(8),'Nota 3'.center(8), 'Promedio'.center(10))
for ced, nom, not1, not2, not3, promedio in zip(id, name, n1, n2, n3, prom):
    print(ced.ljust(10), nom.ljust(20), str(not1).center(8), str(not2).center(8), str(not3).center(8), str(promedio).center(10) )
print(f'Cantidad de estudiantes: {students}')
print(f'Porcentaje de estudiantes aprobados: {porcent_students}')
print(f'Mayor Promedio {alt_prom}')
print(f'promedio del curso: {course_prom}')