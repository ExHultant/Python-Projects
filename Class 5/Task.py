x=1
while x == 1:
    print("Bienvenidos")
    nro_cuenta=int(input("Ingrese numero de cuenta:"))
    cuenta_tipo = int(input("¿Tipo de cuenta?\n1.Ahorro\n2.Corriente\n3.Activo\n"))
    saldoI = float(input("Ingrese el saldo en su cuenta:\n"))
    saldoF = saldoI
    saldoM = saldoI
    y = 1
    while y == 1:
        print("¿Que desea hacer?")
        mov = int(input("1.Deposito\n2.Retiro\n"))
        if mov == 1:
            depo = int(input("Ingrese el monto a depositar: "))
            saldoF = saldoF + depo
        else:
            reti = int(input("Ingrese el monto a retirar: "))
            if reti < saldoF:
                saldoF = saldoF -reti
            else:
                print("Saldo Insuficiente. Saldo Disponible:",saldoF)
            if saldoF < saldoM:
                saldoM=saldoF
        y = int(input("¿Algo mas? 1.Si 2.No \n"))
    if cuenta_tipo == 2:
        interes = 0
        tipo = "Corriente"
    elif cuenta_tipo == 1:
        interes = saldoM * 13/100/12
        tipo = "Ahorro"
    elif cuenta_tipo == 3:
        interes = saldoM * 15/100/12
        tipo = "Activo"
    print("=====================")
    print("Estimado Cliente:")
    print(f"Siendo su numero de cuenta: {nro_cuenta}")
    print(f"Su tipo de cuenta es: {tipo}")
    print(f"Su saldo inicial fue de: {saldoI}")
    print(f"Su saldo minimo es de: {saldoM}")
    print("Intereses:",round(interes),"%")
    print("Su saldo final es de: ",round(saldoF+interes))
    x = int(input("¿Otra cuenta? 1.Si 2.No \n"))