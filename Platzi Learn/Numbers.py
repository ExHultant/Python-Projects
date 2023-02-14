lives = 3
print(type(lives))
temperature = 12.12
print(type(temperature))
number = 450000000000000000000.1
print(number)
number_b = 0.0000000000045
print(number_b)

'''Exercises'''
budget = int(input('Indique su presupuesto del mes de enero: '))
budget_b = int(input('Indique su Presupuesto del mes de Febrero: '))
budget_c = int(input('Indique su Presupuesto del mes de Marzo: '))
total_budget = budget + budget_b + budget_c
print(f'Su presupuesto total de los tres meses sera de: {total_budget}')
prom_budget = total_budget / 3
print(f'El promedio mensual es de: {round(prom_budget)}')
