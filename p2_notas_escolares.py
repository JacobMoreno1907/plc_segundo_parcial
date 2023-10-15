#https://replit.com/@Jacob-OlafOlaf/Estadisticas-de-Notas-Escolares?v=1
total_estudiantes = int(input("Ingrese el número de estudiantes: "))
notas = input("Ingrese las notas de los estudiantes separadas por comas: ")
notas = [float(nota) for nota in notas.split(",")]
promedio = sum(notas) / total_estudiantes
nota_maxima = max(notas)
nota_minima = min(notas)
aprobados = sum(1 for nota in notas if nota >= 60)
reprobados = total_estudiantes - aprobados
print("Promedio de notas:", promedio)
print("Nota más alta:", nota_maxima)
print("Nota más baja:", nota_minima)
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
