#https://replit.com/@Jacob-OlafOlaf/Compra-con-Descuentos-Multiples?v=1
precio = float(input("Ingrese el precio del producto: $"))
categoria = input("Ingrese la categoría (A, B o C): ")
cantidad = float(input("Ingrese la cantidad de unidades compradas: "))
def cpf(precio, categoria, cantidad):
  dc = {
      'A': 0.10,
      'B': 0.05,
      'C': 0.02
  }
  if categoria in dc:
      descuento = dc[categoria]
  else:
      print("Categoría no válida")
      descuento = 0.0
  if cantidad > 10:
      descuento = 0.05
  pf = precio * (1 - descuento)
  return pf
pf = cpf(precio, categoria, cantidad)
print("Precio final después de descuentos: $", pf)
