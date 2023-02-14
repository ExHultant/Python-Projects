vendedores = []
print('Bienvenido')
n = int(input('Ingrese el numero de vendedores: '))
for x in range(n):
    name = input('Ingrese el Nombre del vendedor: ')
    ventas=[]
    rentatotal=0
    for y in range(4):
        vent = float(input(f'ingrese la venta {y+1}: '))
        ventas.append(vent)
        rentatotal += ventas[y]
        vendedores.append([name, vent, rentatotal])
print("Vendedor".ljust(10), 'Venta 1'.center(8), 'Venta 2'.center(8),'Venta 3'.center(8), 'Venta 4'.center(10), 'Renta Total'.center(10))
for name, ventas, rentatotal in zip(name, ventas, rentatotal):
    print(name.ljust(10), str(vent).ljust(10), str(vent).ljust(10), str(vent).ljust(10), str(vent).ljust(10), str(vent).ljust(10))
print(f'el venta total fue de: {rentatotal}')