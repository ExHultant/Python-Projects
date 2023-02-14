#Esto es un comentario :b se puede usar comillas dobles ""
#o comillas simples para escribir comentarios ''

'Variables'
name = 'Ricardo'
age = 20
height = 1.70
print("-----------------")
'Asignacion multiple'
animal, thing, brand = "Dog", "Dekstop" , "Lenovo"
print(animal, thing, brand)
print("-----------------")
'Imprimir en pantalla'
print("Hi! My name is: "+ name)
'print(f()) sirve para comentar en cadena con variables'
print(f'{name} have {age} years old and your height is {height}cm')
'para concatenar puedes utilizar + o ,'
print("-----------------")
'ESTO ES OTRO COMENTARIO MAS LARGO XDDD'
#el programador debe insertar el espacio entre texto y variable
#Python inserta un espacio entre texto y variable
"type  para leer que tipo de clase es la variable"
print(type(name))
number = 7
print('This is a number: ',number)
print(type(number))
realNumber = 1,65
print(realNumber)
print(type(realNumber))
print('----------------------')
'esta es otra manera de imprimir en pantalla usualmente sirven para columnas'
print('{0} have {1} years old and your height is {2}cm'.format(name,age,height))
print('-------------------------')
'Operadores'
'Aritmeticos'
# ** -> Pontencia+
# - -> Cambio de signo
# * -> multiplicacion
# /-> division
# // -> division entera
# % -> modulo o resto de la division
# + and - -> suma o resta
'cambio de signo'
x=6
y=-x
print(f'{x},{y}')
'Asignadores'
#sumador +=
#restante -=
#pontenciador *=
#divisor /=
sumador = 0
nota = 10
sumador += nota
print(sumador)
'Operadores relativos'
#== , !=, > , < , >=, <=
'operadores logicos'
#and, not, or y xor
print(7==8)
print(age >= 18 and age <= 25)
print(18 <= age <= 25)