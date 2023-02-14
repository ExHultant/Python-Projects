#La funcion range permite crear un secuencia de numeros#
print(range(6))
print("---------------------")
#range(valor incial, valor final, paso)#
for x in range(6):
    print(x)
print("---------------------")
for y in range(1,10,2):
    print(y)
print("---------------------")
for z in range(20,5,-5):
    print(z)
print("---------------------")
#usando el cilo for y la funcion range, elabore un programa que pida un numero, comprendido entre
# 1 y 9, y muestre la tabla de multiplicar de dicho numero#
print("Tabla de Multiplicar")
print("Ingrese un numero")
e=int(input())
print("-----------------")
if e < 0:
    print("Error por favor ingrese un numero entero")
else:
    for a in range(1,11):
        d = a*e
        print(f"{e} x {a} = {d}")