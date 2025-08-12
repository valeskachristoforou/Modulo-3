#1. Básico: imprime todos los números enteros del 0 al 100.
print('Ejercicio 1: Básico')
for i in range(101):
    print(i)
print()

# 2. Multiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print('Ejercicio 2: Múltiplos de 2')
for x in range (2, 501, 2):
    print(x)
print()
for x in range(2, 501):
    if x % 2 == 0:
        print(x)
print()
for multdos in range (1, 251):
    print(multdos * 2)

# 3. Contando Vanilla Ice
print('Ejercicio 3: Contando Vanilla Ice')
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
print()

# 4. Wow. Número gigante a la vista

suma = 0
# Recorremos de 0 a 500000, solo los pares (de 2 en 2)
for i in range(0, 500001, 2):
    suma += i  # suma = suma + i

print(f"La suma total de los números pares del 0 al 500000 es: {suma}")
print()
# 4. Contador dinámico:

# Establecer las variables
numInicial = 3
numFinal = 10
multiplo = 2

# Recorrer del número inicial al final (incluido)
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)


