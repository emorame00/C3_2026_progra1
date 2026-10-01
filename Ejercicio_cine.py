# Constantes
PRECIO_ENTRADA = 3500
DESCUENTO_MENOR = 0.20
DESCUENTO_ADULTO_MAYOR = 0.15

# Entrada de datos
edad = int(input("Ingrese su edad: "))
cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))

# Cálculo del subtotal
subtotal = cantidad_entradas * PRECIO_ENTRADA

# Determinar descuento según la edad
if edad < 12:
    descuento = subtotal * DESCUENTO_MENOR
elif edad >= 65:
    descuento = subtotal * DESCUENTO_ADULTO_MAYOR
else:
    descuento = 0

# Calcular total
total = subtotal - descuento

# Mostrar resultados
print("Subtotal: ₡", subtotal)
print("Descuento aplicado: ₡", descuento)
print("Total a pagar: ₡", total)

# Determinar si recibe bebida gratis
if cantidad_entradas >= 4:
    print("El cliente recibe 1 bebida gratis.")
else:
    print("El cliente no recibe bebida gratis.")