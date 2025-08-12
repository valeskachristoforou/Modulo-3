# 1. Actualizar valores en diccionarios y listas
matriz = [[10, 15, 20], [3, 7, 14]]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios solicitados
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# 2. Recorrer lista de diccionarios
print("=== Lista de cantantes ===")
for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

# 3. Obtener valores específicos
print("\n=== Nombres ===")
for cantante in cantantes:
    print(cantante["nombre"])

print("\n=== Países ===")
for cantante in cantantes:
    print(cantante["pais"])

# 4. Recorrer diccionario con listas como valores
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("\n=== Datos de Costa Rica ===")
for clave, lista in costa_rica.items():
    print(f"{len(lista)} {clave.upper()}")
    for elemento in lista:
        print(elemento)
