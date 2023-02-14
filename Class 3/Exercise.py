#elabore un programa que pida el nro de votos obtenidos por tres candidatos
# determine el resultado de la eleccion#
print("Ingrese el nro de votos del primer candidato")
cant1 = input()
print("Ingrese el nro de votos del segundo candidato")
cant2 = input()
print("Ingrese el nro de votos del tercer candidato")
cant3 = input()
if cant1 > cant3 and cant1 > cant2:
    print("El candidato 1 gano con ", cant1, " de votos")
elif cant1 == cant2:
    print(f'ha habido un empate entre candidato 1 y candidato 2')
elif cant2 > cant3 and cant2 > cant1:
    print("El candidato 3 gano con ", cant2, " de votos")
elif cant2 == cant3:
    print(f'ha habido un empate entre candito 2 y candidato 3')
elif cant3 > cant1 and cant3 > cant2:
    print("El candidato 3 gano con ", cant3, " de votos")
elif cant3 == cant1:
    print(f'ha habido un empate entre candidato 3 y candidato 1')
elif cant2 == cant1:
    print(f'ha habido un empate entre candidato 2 y candidato 1')