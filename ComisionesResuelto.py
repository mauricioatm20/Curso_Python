nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

#ventas = int(ventas)
#comision = ventas * 13/100
#comision = round(comision, 2)

comision = round(ventas * 13 / 100, 2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")