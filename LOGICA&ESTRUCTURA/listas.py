#Clase 4: Estructuras de Datos (Listas)
#Ahora tu programa suma números, pero... ¿y si queremos recordar qué productos compramos? Si el cliente pregunta "¿Qué compré?", el programa ya lo olvidó porque solo guardó el número final.
#Para guardar muchos datos en una sola variable usamos Listas [].
#Operaciones básicas con listas:
"""
Crear una lista: productos = []
Añadir algo: productos.append("Smartphone")
Ver cuántos hay: len(productos)
"""
#Tu Reto Nivel 4: "El Ticket Detallado"
#Vamos a mejorar el programa anterior para que al final nos dé un ticket real.

"""
Antes del bucle, crea una lista vacía llamada carrito.
Dentro del bucle, cada vez que el usuario introduzca un producto, 
añade el nombre del producto a la lista carrito.
Al final de todo (cuando el usuario diga "n"), usa un bucle for para imprimir 
la lista de productos comprados.

"""
#Ejemplo de cómo imprimir la lista:
"""
print("Has comprado los siguientes artículos:")
for item in carrito:
    print(f"- {item}")
      """

################################################################
continuar = "s"
total_factura = 0
#1. Se crea la lista carrito vacia para almacenar los nombres de los productos comprados.
carrito =[]


while continuar == "s":
 nombre: str = input("Escribe el nombre del producto: ")
 carrito.append(nombre) #2. Se añade el nombre del producto a la lista carrito usando el método append.
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
#3. Al final, se imprime la lista de productos comprados usando un bucle for que recorre cada elemento de la lista carrito e imprime su nombre.
print("Has comprado los siguientes artículos:")
for nombre in carrito:
    print(f"- {nombre}") 