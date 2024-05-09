#calcular el sueldo neto de un trabajador conociendo las horas trabajadas, tarifa de hora, imposiciones.

horasTrabajadas = int(input('Ingrese el total de horas semanales trabajadas'))

tarifaHora = int(input('Ingrese la tarifa por hora'))

resultBrut = horasTrabajadas*tarifaHora

imposicionesIsapre = resultBrut * 0.07 
imposicionesAfp = resultBrut * 0.12

imposicionesTotal = imposicionesAfp + imposicionesIsapre

resultNeto = resultBrut - imposicionesTotal

print(resultBrut)
print(imposicionesAfp)
print(imposicionesIsapre)
print(resultNeto)

