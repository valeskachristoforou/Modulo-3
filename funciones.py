def mt_a_cm(metros): #metros = 2.33
    cm = metros*100 #cm = 2.33 * 100 = 233
    return cm # <- 233


def saludar():
    print("¡Hola!")

nombre = "Diego"

def saludar_nombre(nombre): #nombre = "Diego"
    otra_variable = ":)"
    print(f"¡Hola {nombre} {otra_variable}!")
    #print("¡Hola "+nombre+"!")


saludar()
saludar()
saludar()
saludar()
saludar()
saludar()

saludar_nombre("Elena")
saludar_nombre("Juana")
saludar_nombre(nombre) #nombre = "Diego"

centimetros = mt_a_cm(1.55) #centimetros = 155

def mt_a_cm_y_mm(metros): #metros = 2.33
    cm = mt_a_cm(metros) #cm = 233
    mm = metros * 1000 #mm = 2.33 * 1000 = 2330
    if mm > 2000: 
        print("wow son muchos mm")
    return (cm, mm) #regresa 233, 2330


centimetros, milimetros = mt_a_cm_y_mm(2.33) #centimetros = 233, milimetros = 2330
print(centimetros, milimetros)

def saludito(nombre="Elena", apellido="De Troya"): #nombre = "Elena", apellido = "De Arco"
    print(f"¡Buen día {nombre} {apellido}! ¿cómo va todo?")

saludito()
saludito("Juana") #¡Buen día Juana De Troya! ¿cómo va todo? 
saludito(apellido="De Arco") #¡Buen día Elena De Arco" ¿cómo va todo?
saludito(apellido="De Arco", nombre="Juana") #¡Buen día Juana de Arco! ¿cómo va todo?

#Función que reciba un lista y que regrese la suma de los valores mayores a 10
#Ej. [1, 2, 3, 11, 12]. Regresar 23

def suma_mayores_a_diez(lista):
    suma = sum(valor for valor in lista if valor > 10)
    return suma
numeros = [1, 2, 3, 15, 15]
resultados = suma_mayores_a_diez(numeros)
print(resultados)

#Función que reciba un lista y que regrese los dos números mayores
#Ej. [4, 5, 1, 2, 6]. Regresar (6, 5)
def dos_numeros_mayores(lista_dos):
    if len(lista_dos) < 2:
        return None
    numeros_mayores = sorted(lista_dos, reverse = True)
    return numeros_mayores [0], numeros_mayores[1]

numeros_mayores = [4, 5, 1, 2, 6]
resultados = dos_numeros_mayores(numeros_mayores)
print(resultados)
    

#Función que reciba un lista y reemplace cualquier número negativo por 0. Regresa el lista SIN números negativos. 
#Ej. Recibes: [1,5,10,-2], Regresas [1,5,10,0]
def numeros_negativos (lista_tres):
    nueva_lista_tres = []
    for numero in nueva_lista_tres:
        if numero < 0:
            nueva_lista_tres.append(0)
        else: 
            nueva_lista_tres.append(numero)
    return nueva_lista_tres 

numeros_mayores_cero = [1,5,10,-2]
resultados = numeros_negativos(numeros_mayores_cero)
print(resultados)



#Función que reciba una lista y un número, y regrese todas las posiciones (índices) donde aparece ese número Ej. recibe ([1, 5, 3, 5, 2, 5], 5) regresa [1, 3, 5]