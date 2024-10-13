pip install pyfiglet
from pyfiglet import Figlet
figlet = Figlet()
import random
from pyfiglet import Figlet

# Crear una instancia de Figlet
figlet = Figlet()

# Solicitar al usuario la fuente
fuente = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ")

# Si no se ingresa una fuente, se selecciona una aleatoria
if not fuente:
    fuentes_disponibles = figlet.getFonts()
    fuente = random.choice(fuentes_disponibles)

# Configurar la fuente seleccionada en Figlet
try:
    figlet.setFont(font=fuente)
except:
    print(f"La fuente '{fuente}' no es válida. Se seleccionará una fuente aleatoria.")
    fuentes_disponibles = figlet.getFonts()
    fuente = random.choice(fuentes_disponibles)
    figlet.setFont(font=fuente)

# Solicitar al usuario el texto
texto = input("Ingrese el texto que desea imprimir: ")

# Imprimir el texto con la fuente seleccionada
print(figlet.renderText(texto))

