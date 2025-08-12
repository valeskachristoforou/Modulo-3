#Crea la funcion  Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6  # Cambiar 3 por 6

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"  # Cambiar nombre del primer cantante

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"  # Cambiar "Cancún" por "Monterrey"

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431  # Cambiar valor de latitud


# Función 2: Iterar a través de una lista de diccionarios e imprimir cada llave y valor
def iterarDiccionario(lista):
    for dic in lista:
        # Forma básica, imprimir cada llave y valor en líneas separadas
        # for llave, valor in dic.items():
        #     print(f"{llave}: {valor}")
        # print()

        # BONUS: imprimir en formato "llave - valor, llave - valor"
        salida = []
        for llave, valor in dic.items():
            salida.append(f"{llave} - {valor}")
        print(", ".join(salida))


# Función 3: Obtener valores de una lista de diccionarios según la llave dada
def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])


# Función 4: Iterar un diccionario con listas e imprimir cantidad y elementos
def imprimirInformacion(diccionario):
    for clave in diccionario:
        lista = diccionario[clave]
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()  # línea en blanco para separar


# Aquí puedes hacer pruebas si quieres, por ejemplo:
if __name__ == "__main__":
    # Probamos las funciones con los datos dados:
    print("Matriz actualizada:", matriz)
    print("Cantantes actualizados:", cantantes)
    print("Ciudades actualizadas:", ciudades)
    print("Coordenadas actualizadas:", coordenadas)

    print("\nIterar diccionario:")
    cantantes2 = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"},
        {"nombre": "José José", "pais": "México"},
        {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
    ]
    iterarDiccionario(cantantes2)

    print("\nIterarDiccionario2 por 'nombre':")
    iterarDiccionario2("nombre", cantantes2)

    print("\nIterarDiccionario2 por 'pais':")
    ite
n iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente
