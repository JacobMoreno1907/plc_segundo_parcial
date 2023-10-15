#https://replit.com/@Jacob-OlafOlaf/Plan-de-Ahorro-para-la-Jubilacion?v=1
def calcular_pago_mensual(FV, r, n, t):
  PMT = (FV * r) / (((1 + r) ** n - 1) * (1 + r) ** -t)
  return PMT
edad_actual = int(input("Ingrese su edad actual: "))
edad_jubilacion = int(input("Ingrese la edad a la que planea jubilarse: "))
cantidad_deseada = float(input("Ingrese la cantidad deseada para la jubilación: $"))
rendimiento_anual = float(input("Ingrese la tasa de interés anual esperada (porcentaje): "))
r = (rendimiento_anual / 100) / 12
n = (edad_jubilacion - edad_actual) * 12
t = edad_jubilacion - edad_actual
pago_mensual = calcular_pago_mensual(cantidad_deseada, r, n, t)
print("Debe ahorrar $", pago_mensual, "mensualmente para alcanzar la jubilación de: $", cantidad_deseada)
print("Para jubilarse faltan:", t, "años")
