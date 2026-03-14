#Clase 3: Bucles (Loops) - El poder de la repetición
#Hasta ahora, tu programa se ejecuta una vez y se apaga. ¿Qué pasa si el cliente quiere comprar varios productos diferentes? Necesitamos que el programa se repita.
#Existen dos tipos de bucles:
"""
while: Se repite mientras una condición sea verdadera (útil para menús).
for: Se repite un número fijo de veces o sobre una lista.
"""
#Ejemplo de while:

import nt


continuar = "s"
while continuar == "s":
    print("Procesando compra...")
    continuar = input("¿Quieres agregar otro producto? (s/n): ")

print("Gracias por su compra.")

#Reto Nivel 3: "La Superfactura"
#Vamos a crear una aplicación que permita comprar varios productos.

"""
Continuando con la apliacion de los auriculares inalámbricos, vamos a hacerla más completa.
Quiero que hagas lo siguiente:
Crea una variable llamada total_factura que empiece en 0.
Usa un bucle while que pregunte al usuario: "¿Quieres añadir un producto? (s/n)".
Si dice que "s":
Pide el nombre y el precio del producto.
Súmalo a la variable total_factura.
Si dice que "n":
Termina el bucle.
Muestra el total de todos los productos sumados.
Aplica un descuento del 10% solo si el total de la factura supera los $2000.
Pista: Para ir sumando valores a una variable usa: total_factura += precio.

"""

continuar = "s"
total_factura = 0

while continuar == "s":
 nombre: str = input("Escribe el nombre del producto: ")
 precio_base: float = float(input("Escribe el precio del producto: "))
 cantidad: int = int(input("Escribe la cantidad que deseas comprar:"))
 subtotal = precio_base * cantidad
 iva = subtotal * 0.21
 total_final = subtotal + iva
 total_factura += total_final
 continuar = (input("¿Quieres añadir otro producto? (s/n): "))
if total_factura >2000:
   descuento = total_factura * 0.10
   total_factura = total_factura - descuento
   print(f"Total de la factura después del descuento: ${round(total_factura,2)}")
else:
    print(f"Total de la factura: ${round(total_factura,2)}")
