# 1. Imprime "Hola, mundo"
print("¡Hola, mundo!")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Valeska"
print("Hola", nombre) # con una coma
#Hola&Valeska
print("Hola", nombre, sep="&")
print("Hola, "+nombre) #LITERAL SOLO PEGAR LAS CADENAS

# 3. Imprimir "Hola 111!" con el número en una variable
numero = 111
print( "Hola", numero, "!" ) # con una coma
print ("Hola "+str(numero)+"!") #Porque estoy convirtiendo mi numero en string? String los hace de la misma clase (Casteamos la variable numero a string)

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "papas fritas"
comida2 = "pollo asado"
print( "Me encanta comer {} y {}".format(comida1, comida2)) # con .format()
comidas = "Me encanta comer {} y {}" .format(comida1, comida2) #Ejemplo compañero Daniel H.
print(comidas)
print(f"Me encanta comer {comida1} y {comida2}")
print(f"Me encanta comer {comida1} y {comida2}") # con una cadena f

nombre = "Valeska"
edad = 34
mensaje = f'Hola, mi nombre es {nombre} y tengo {edad} años.'
print(mensaje)