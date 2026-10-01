# Compra en tienda

producto = input("Ingresar producto:")
precio = float(input("Precio unitario:"))
cantidad = int(input("Cantidad:"))
total = precio * cantidad
print("Total a pagar:", total)
pago = float(input("Ingrese el monto a pagar:"))
vuelto = pago - total
print("Su vuelto es:", vuelto)
print("Gracias por su visita")