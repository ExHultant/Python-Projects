'Elabore un programa que calcule el indice de masa corporal'
peso = int(input('indique su peso: '))
estatura = float(input('indique su estatura: '))
imc = round(peso / estatura ** 2)
print("Su indice de masa corporal es: ",imc)