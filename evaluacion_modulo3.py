ARCHIVO_TAREAS = "tareas.txt"

def cargar_tareas():
    tareas =[]
    try:
        with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                tarea = linea.strip()
                if linea:
                    partes = linea.split('|', 1)
                    if len(partes) ==2:
                        descripcion, estado_str = partes
                        completada = estado_str == "completada"
                        tareas.append({
                            "descripcion": descripcion,
                            "completada": completada
                        })
                        
    except FileNotFoundError:
        return []
    
    return tareas 

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as archivo:
        for tarea in tareas:
            estado_str = "completada" if tarea["completada"] else "pendiente"
            archivo.write(f"{tarea['descripcion']}|{estado_str}\n")
            
def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    
def agregar_tarea(tareas):
    descripcion = input("Escribe la descripción de la tarea: ")
    
    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"tarea '{descripcion}' agregada exitosamente.")
    
def ver_tareas(tareas):
    print("\n--- Lista de Tareas ---")
    if not tareas:
        print("No hay tareas pendientes.")
        return
    for i, tarea in enumerate(tareas):
        estado = "completada" if tarea["completada"] else "pendiente"
        print(f"{i + 1}. [{estado}] {tarea['descripcion']}")
        
def marcar_completada(tareas):
    ver_tareas(tareas)
    if not tareas:
        return
    
    try:
        numero_tarea = int(input("ingresa el número de la tarea a marcar como completada: "))
        
        if 1 <= numero_tarea <= len(tareas):
            tareas[numero_tarea - 1]["completada"] = True
            guardar_tareas(tareas)
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea no valido.")
    except ValueError:
        print("Entrada no valida. Por favor ingresa un número.")
        
def eliminar_tarea(tareas):
    ver_tareas(tareas)
    if not tareas:
        return
    
    try:
        numero_tarea = int(input("Ingresa el numero de la tarea a eliminar:"))
        
        if 1 <= numero_tarea <= len(tareas):
            tarea_eliminada = tareas.pop(numero_tarea - 1)
            guardar_tareas(tareas)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada exitosamente.")
    
    except ValueError:
        print("Entrada no valida. Por favor ingresa un número.") 
             
def main():
    tareas = cargar_tareas()
    
    while True:
        mostrar_menu()
        opcion = input ("Elige una opcion: ")
        
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("Gracias por usar el gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")     
            
if __name__ == "__main__":
    main()               
    
    