#LISTAS#
CED=[]
print(CED)
#Mide la longitud de las listas#
print(len(CED))
print("-------------")
r = 'S'
while r == 'S':
    print("Ingrese su cedula")
    cedula= input()
    CED.append(cedula)
    print(CED)
    r = input("¿Otra cedula? S/N")
for x in range(len(CED)):
    print(CED[x])
print("================")
for cedula in CED:
    print(cedula)