import random
import math

#BOOLEANS
mayor_edad = True
tiene_bigote = False

#NUMERALES
edad = 25 #Entero (sin decimales)
altura = 2.05 #Flotante (con decimales)

edad_flotante = float (edad) #Transformar mi valor en flotante
print(edad_flotante)

altura_entera = int(altura) #Transformar mi valor en entero
print(altura_entera)

decimal = 3.55
print(int(decimal)) #3
#Round: redondear al valor entero más cercano
print(round(decimal)) #4
print(round(decimal, 1)) #3.6

numero_negativo = -10
print(abs(numero_negativo))

numero_alcuadrado = pow(2, 2)
print(numero_alcuadrado)

suamtoria = sum((1, 2, 3)) #Recibe una lista y regresa la sumatoria de esta
print(suamtoria)

numero_maximo = max(2, 3, 1) #Recibe n cantidad de números y regresa el mayor
print(numero_maximo)

numero_minimo = min(2, 3, 1) #Recibe n cantidad de números y regresa el menor
print(numero_minimo)

num_aleatorio = random.randint(5, 10) #Número entero aleatorio entre 5 y 10

decimal_aleatorio = random.uniform(-10, 10) #Númeor decimal aleatorio entre -10 y 10
print(num_aleatorio)
print(decimal_aleatorio)

'''
Genera 5 números enteros aleatorios enteros entre 10 y 10,000 usando la librería random.
Para cada número:
Muestra su valor y su tipo de dato usando la función type().
Muestra cuántos dígitos tiene utilizando len().*
Muestra el resultado con un mensaje descriptivo.
'''
num1 = random.randint(10, 10000)
num2 = random.randint(10, 10000)
num3 = random.randint(10, 10000)
num4 = random.randint(10, 10000)
num5 = random.randint(10, 10000)

print(f"El valor es: {num1}, su tipo es: {type(num1)}, y la cantidad de digitos es: {len{str(num1)}}")


'''
Pide al usuario que ingrese dos números (enteros o decimales).
Para cada número, calcula y muestra:
La raíz cuadrada (de su valor absoluto).
Su valor elevado a la tercera potencia.
Su valor absoluto.
El redondeo hacia arriba (ceil) y hacia abajo (floor).
Luego, muestra las operaciones entre ambos números:
Suma, resta, multiplicación y división.
Máximo y mínimo de los dos números.
Potencia del primer número elevado al segundo (math.pow()).
'''

numero1 = float(input("Ingresa el primero número: "))
numero2 = float(input("Ingresa el segundo número: "))

print("Para el primer número")