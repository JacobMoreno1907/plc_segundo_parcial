#https://replit.com/@Jacob-OlafOlaf/Calculadora-de-Nutrientes-en-Recetas?v=1
def calcular_nutrientes_totales(ingredientes, cantidades, info_nutricional):
  total_nutrientes = {"calorias": 0, "proteinas": 0, "carbohidratos": 0, "grasas": 0}
  for i, ingrediente in enumerate(ingredientes):
      cantidad = cantidades[i]
      nutricion = info_nutricional[ingrediente]
      for nutriente, valor_por_100g in nutricion.items():
          total_nutrientes[nutriente] += (valor_por_100g / 100) * cantidad
  return total_nutrientes
ingredientes = []
cantidades = []
info_nutricional = {}
n = int(input("Ingrese el número de ingredientes en la receta: "))
for _ in range(n):
  ingrediente, cantidad = input("Ingrese el nombre y la cantidad del ingrediente (nombre cantidad): ").split()
  ingredientes.append(ingrediente)
  cantidades.append(float(cantidad))
  info_nutricional[ingrediente] = {
      "calorias": float(input(f"Calorías por cada 100g de {ingrediente}: ")),
      "proteinas": float(input(f"Proteínas por cada 100g de {ingrediente}: ")),
      "carbohidratos": float(input(f"Carbohidratos por cada 100g de {ingrediente}: ")),
      "grasas": float(input(f"Grasas por cada 100g de {ingrediente}: "))
  }
total_nutrientes = calcular_nutrientes_totales(ingredientes, cantidades, info_nutricional)
print("\nNutrientes totales en la receta:")
for nutriente, valor in total_nutrientes.items():
  unidad = "kcal" if nutriente == "calorias" else "g"
  print(f"{nutriente.capitalize()}: {valor:.2f} {unidad}")
