'''
=========================================
    Calculadora Pythonirica!
=========================================
Elige una opción:

1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Dividir dos números (con validación de 0)
5. Calcular el cuadrado y cubo de un número
6. Contar cuántas letras tiene una palabra
7. Saber si una palabra es corta, media o larga
8. Calcular el promedio de tres números
9. Comparar tres números y decir cuál es el mayor
10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales
11. Salir de la Súper Calculadora

=========================================
Recomendaciones:
-Usar try-except
-Revisar que los números sean válidos para cada acción
-Eliminar espacios y validar que hayan ingresado una palabra en los casos de palabras
-En el promedio, redondear
BONUS:
-Uso de while para mostrar múltiples veces el menú
-Uso de while para pedir los inputs
-Contador general para saber cuántas veces ha usado el menú
-Contador individual para saber cuántas veces ha usado cada opción del menú
-Mostrar los contadores en un mensaje al salir
'''
print("""=========================================
    Calculadora Pythonirica!
=========================================
Elige una opción:

1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Dividir dos números (con validación de 0)
5. Calcular el cuadrado y cubo de un número
6. Contar cuántas letras tiene una palabra
7. Saber si una palabra es corta, media o larga
8. Calcular el promedio de tres números
9. Comparar tres números y decir cuál es el mayor
10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales
11. Salir de la Súper Calculadora""")

opcion = int(input('Elige una opción (1-11): '))

if opcion == 1:
    try:
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        print('Resultado:', a + b)
    except:
        print('Error: Ingresa solo números válidos.')

if opcion == 2:
    try:
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        print('Resultado:', a - b)
    except:
        print('Error: Ingresa solo número validos.')

if opcion == 3:
    try:
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        print('Resultado:', a * b)
    except:
        print('Error: Ingresa solo número validos.')


def contar_vocales(word):
    contador = 0
    vocales = "aeiouAEIOU"
    for letra in word:
        if letra in vocales:
            contador +=1
    return contador