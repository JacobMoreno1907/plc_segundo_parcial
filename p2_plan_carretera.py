#https://replit.com/@Jacob-OlafOlaf/Planificacion-de-Viaje-por-Carretera?v=1
millas = float(input("Ingrese la distancia en millas: "))
rendimiento = float(input("¿Cuál es el rendimiento de millas por galón de gasolina? "))
precio = float(input("¿Cuál es el precio actual del galón de gasolina? "))
dias = float(input("¿Cuántos días planeas de viaje? "))
if dias >= 3:
    precio *= 1.5
else:
    precio *= 1
costo_total = (millas / rendimiento) * precio * dias
print("El costo de todo el viaje es de:", costo_total)
