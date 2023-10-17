https://replit.com/join/jsmkiiuckj-jacob-olafolaf
ruedas = float(input("Inserte el número de ruedas del vehículo"))
combustible = input("Inserte el tipo de combustible (gasolina/diésel/eléctrico)")
emisiones = float(input("Ingrese la cantidad de emisiones de CO2, la unidad de medida es (g/km)"))
if ruedas <= 4 and combustible == "eléctrico":
  print("El vehículo es eléctrico")
elif ruedas > 4 and combustible == "gasolina" and emisiones >= 150:
  print("El vehículo usa como combustible gasolina es grande y contaminante")
elif combustible == "diésel":
  print("El vehículo usa como combustible el diésel")
else:
  print("Esa opción no es correcta")
