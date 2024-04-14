from pyfiglet import Figlet
import random

figlet = Figlet()
fuentes_disponibles = figlet.getFonts()

fuente_seleccionada = input(f"Seleccione una fuente ({', '.join(fuentes_disponibles)}) o presione Enter para seleccionar aleatoriamente: ")
if fuente_seleccionada == "":
    fuente_seleccionada = random.choice(fuentes_disponibles)
    print(f"Fuente seleccionada aleatoriamente: {fuente_seleccionada}")
elif fuente_seleccionada not in fuentes_disponibles:
    print("La fuente seleccionada no es válida, seleccione una fuente de la lista")
    exit()

figlet.setFont(font=fuente_seleccionada)

texto_imprimir = input("Ingrese un texto para imprimir: ")

print(figlet.renderText(texto_imprimir))

