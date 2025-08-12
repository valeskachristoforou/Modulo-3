#Para ejecutar en Windows: python nombre_archivo.py
#Para ejecturar en Mac: python3 nombre_archivo.py
print ("¡Hola mundo!")

'''
Un comentario es una anotación 
para los desarrolladores
y no afecta el funcionamiento 
de mi código fuente
'''

variable1 = 1
variable1 = "uno" #sobreescribiendo la variable, estoy cambiando el tipo de dato de esta
print(variable1)

print (type(variable1))

#Casteo: el cambiar de tipo de dato
x = str(3) #"3" como texto
print(x)
x = int(3.3) #convierte en número entero el valor que tengo
print (x)
x = float(3) #3.0
print (x)

numero = 74
print ("El mejor grupo es el:" + str(numero))

texto = "Puede tener comillas dobles"
otro_texto = 'o comillas simples'
