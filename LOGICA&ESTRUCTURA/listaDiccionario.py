#Nivel 5: Listas de Diccionarios.
#En lugar de guardar solo el texto del nombre en la lista, 
# vamos a guardar un diccionario que contenga toda la información de ese producto.

# En lugar de esto:
# carrito.append(nombre)

# Haremos esto:
"""
producto_completado = {
    "nombre": nombre,
    "precio_total": total_final
}
carrito.append(producto_completado)

"""
#Tu Reto Final de "Nivel Plata": El Ticket Profesional
#Quiero que modifiques tu código para que el ticket final se vea así:

"""
--- RESUMEN DE COMPRA ---
- Smartphone: $604.99
- Funda: $24.2
- Cargador: $36.3
-------------------------
TOTAL FACTURA: $665.49

"""
#Instrucciones:
"""

Dentro del while, crea el diccionario producto_completado con las llaves "nombre" y "precio_total".
Añade ese diccionario a la lista carrito.
En el bucle for del final, recuerda que ahora cada elemento (llamémoslo item) es un diccionario. Tendrás que imprimirlo así:
print(f"- {item['nombre']}: ${round(item['precio_total'], 2)}")

"""
continuar = "s"
total_factura = 0
#1. Se crea la lista carrito vacia para almacenar los nombres de los productos comprados.
carrito =[]



while continuar == "s":
 nombre: str = input("Escribe el nombre del producto: ")
 precio_base: float = float(input("Escribe el precio del producto: "))
 cantidad: int = int(input("Escribe la cantidad que deseas comprar:"))
 subtotal = precio_base * cantidad
 iva = subtotal * 0.21
 total_final = subtotal + iva
 total_factura += total_final
 producto_completo = {
        "nombre": nombre,
        "precio_total": total_final
    }
 carrito.append(producto_completo)
 continuar = (input("¿Quieres añadir otro producto? (s/n): "))
if total_factura >2000:
   descuento = total_factura * 0.10

   total_factura = total_factura - descuento
   print(f"----TOTAL FACTURA----: ${round(total_factura,2)}")
else:
    print(f"Total de la factura: ${round(total_factura,2)}")
#3. Al final, se imprime la lista de productos comprados usando un bucle for que recorre cada elemento de la lista carrito e imprime su nombre.
print("RESUMEN DE COMPRA:")
print("-------------------------")
for producto_completo in carrito:
    print(f"- {producto_completo['nombre']}: ${round(producto_completo['precio_total'], 2)}")
    
