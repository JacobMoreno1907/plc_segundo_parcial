#https://replit.com/@Jacob-OlafOlaf/Calculadora-de-Calorias-Quemadas?v=1
def calcular_calorias_quemadas(peso, duracion, actividad):
  if actividad == "correr":
      calorias_por_minuto = 11.4
  elif actividad == "nadar":
      calorias_por_minuto = 7.0
  elif actividad == "andar en bicicleta":
      calorias_por_minuto = 5.8
  total_calorias_quemadas = calorias_por_minuto * duracion
  return total_calorias_quemadas
peso = float(input("Ingrese su peso en kg: "))
duracion = int(input("Ingrese la duración de la actividad en minutos: "))
actividad = input("Ingrese el tipo de actividad (correr, nadar, andar en bicicleta, etc.): ")
calorias_quemadas = calcular_calorias_quemadas(peso, duracion, actividad)
print("Calorías quemadas durante", duracion, "minutos de", actividad, ":", calorias_quemadas, "kcal")
