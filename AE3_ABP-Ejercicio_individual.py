cantidad_productos = int(input('¿Cuántos productos compró?'))
compras_previas = int(input('¿Cuántas compras ha hecho antes?'))
total_compra = float(input('¿Cúal fue el total de compra?'))
dia_promocion = input('¿Es un dia especial de promocion? (si/no): ' ).lower()

descuento_total = 0

if cantidad_productos >= 10:
     descuento_total += 10

if compras_previas > 5:
    descuento_total += 5
    
if total_compra >= 500:
    descuento_total += 7

if dia_promocion == "si":
    descuento_total += 15

if descuento_total > 30:
    descuento_total = 30

print(f'El descuento total aplicado es: {descuento_total:}%')

#Clasificación del tipo de cliente (solo para cumplir con elif y else)
if cantidad_productos > 10:
    print('Cliente VIP')
elif compras_previas > 5:
    print('Cliente frecuente')
else:
    print('Cliente nuevo')

if compras_previas > 5 and dia_promocion == 'si':
    print('¡Cliente frecuente en día de promo! Descuento adicional del 2%')
    descuento_total += 2