#Elabore un algoritmo que calcule el bono por venta que recibira un
#vendedor el bono por venta es un porcentaje del monto en BS
#Vendidos por el vendedor el porcentaje depende del departamento
#Departamentos:
#Ropa == 0.5%
#Juguete == 0.75%
#Lenceria == 0.8%
ropa = 0.5
toys = 0.75
lenc = 0.8
name = str(input("Ingrese Nombre y apellido"))
dep = int(input("Ingrese su departamento: \n 1.Ropa \n 2.Juguete \n 3.Lenceria"))
mont_Vendido = float(input("Ingrese el monto vendido"))
print('Vendedor:'+name)
if dep == 1:
   print('Departamento: Ropa')
   comision = mont_Vendido * ropa/100
   print('% Comision:', ropa)
elif dep == 2:
   print('Departamento: Juguete')
   comision = mont_Vendido * toys / 100
   print('% Comision:', toys)
elif dep == 3:
   print('Departamento: Lenceria')
   comision = mont_Vendido * lenc / 100
   print('% Comision:', lenc)
print(f'Monto Vendido:{mont_Vendido}')
print('Comision:', comision)

