import random #importación de la libreria random
import modulo 
import paquetes.saludos
from paquetes.matematicas import suma, resta

numero_aleatorio = random.randint (1, 10)
print(numero_aleatorio)

modulo.hola()
paquetes.saludos.saludar("Elena de Troya")
print("¿Cuanto es 5+3?",suma (5,3))
#print("¿Cuanto es 5-3?", resta(5,3))