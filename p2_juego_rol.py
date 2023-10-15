#https://replit.com/@Jacob-OlafOlaf/Simulacion-de-Juego-de-Rol-RPG?v=1
import random
print("Juego de rol (RPG)")
opciones = {"Mago", "Guerrero", "Arquero"}
print(opciones)
personaje = input("Elige un personaje: ")
if personaje not in opciones:
      print("Esa opción no es válida")
else:
      print("Hay un monstruo que te quiere atacar, lanza un dado para defenderte")
      ataque = input("¿Quieres lanzar el dado? (Sí/No): ")
      dado = random.randint(1, 6)
      if ataque == "Sí":
          if dado >= 3:
              print("Triunfaste en la batalla contra el monstruo")
          else:
              print("Perdiste la batalla contra el monstruo")
      elif ataque == "No":
          print("Perdiste la batalla contra el monstruo")
      else:
          print("No es posible esa respuesta")
