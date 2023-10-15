#https://replit.com/@Jacob-OlafOlaf/Conversion-de-Unidades-de-Medida?v=1
def convertir_unidades(cantidad, unidad_origen, unidad_destino):
  if unidad_origen == "millas" and unidad_destino == "kilometros":
      resultado = cantidad * 1.60934
  elif unidad_origen == "kilometros" and unidad_destino == "millas":
      resultado = cantidad / 1.60934
  elif unidad_origen == "litros" and unidad_destino == "galones":
      resultado = cantidad * 0.264172
  elif unidad_origen == "galones" and unidad_destino == "litros":
      resultado = cantidad / 0.264172
  elif unidad_origen == "fahrenheit" and unidad_destino == "celsius":
      resultado = (cantidad - 32) * 5/9
  elif unidad_origen == "celsius" and unidad_destino == "fahrenheit":
      resultado = (cantidad * 9/5) + 32
  else:
      resultado = "Conversión no válida"
  return resultado
print("Bienvenido al programa de conversión de unidades.")
cantidad = float(input("Ingrese la cantidad a convertir: "))
unidad_origen = input("Ingrese la unidad de origen: ")
unidad_destino = input("Ingrese la unidad de destino: ")
resultado = convertir_unidades(cantidad, unidad_origen, unidad_destino)
if resultado == "Conversión no válida":
  print("No se puede realizar la conversión")
else:
  print(cantidad, unidad_origen, "es igual a", resultado, unidad_destino)
