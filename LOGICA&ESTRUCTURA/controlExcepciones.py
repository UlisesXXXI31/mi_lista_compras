#Clase 7: Manejo de Errores (Haciendo la App "Indestructible")
#¿Qué pasa si ahora ejecutas tu programa y, cuando te pide el precio, escribes "gratis" en lugar de un número?
#¡BOOM! El programa se cierra con un error rojo horrible (ValueError).
#Como experto, no puedes permitir que tu aplicación se rompa. Para eso usamos el bloque try ... except.
#Ejemplo:

"""
try:
    precio = float(input("Dime el precio: "))
except ValueError:
    print("¡Error! Debes ingresar un número válido.")
    # Aquí puedes decidir qué hacer, como pedirlo de nuevo

"""
#Tu Reto Nivel 7: "La App a prueba de balas"

#Vamos a proteger tu bucle principal para que no se detenga 
# si el usuario comete un error al escribir números.

"""
Envuelve la parte donde pides el precio y la cantidad dentro de un bloque try.
Usa except ValueError: para capturar el error si el usuario escribe letras.
Si ocurre un error, muestra un mensaje: "Entrada no válida. Este producto no se añadirá al carrito." y usa la instrucción continue.
¿Qué hace continue? Salta el resto del código del bucle y vuelve arriba para preguntar por el siguiente producto (o si desea continuar).
"""

#Estructura de ayuda:

"""
while continuar == "s":
    nombre = input("Nombre: ")
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Error en los datos. Intenta de nuevo.")
        continue # Esto hace que el programa vuelva al principio del 'while'
    
    # ... resto de tu código (calcular total, añadir a carrito, etc.)
"""
continuar = "s"
total_factura = 0
#1. Se crea la lista carrito vacia para almacenar los nombres de los productos comprados.
carrito =[]

def calcular_total_item(precio, cantidad):
    subtotal = precio * cantidad
    iva = subtotal * 0.21
    total_final = subtotal + iva
    return total_final

def aplicar_descuento(total_factura):
    if total_factura >2000:
      descuento = total_factura * 0.10
      total_factura = total_factura - descuento
      print(f"----DESCUENTO----: ${round(descuento,2)}")
    else:
     print(f"No se aplicó descuento.")  
    return total_factura

def mostrar_ticket(lista_productos, total_final):
    print("RESUMEN DE COMPRA:")
    print("-------------------------")
    for producto_completo in lista_productos:
        print(f"- {producto_completo['nombre']}: ${round(producto_completo['precio_total'], 2)}")
    print(f"TOTAL FACTURA: ${round(total_final,2)}")

while continuar == "s":
    nombre: str = input("Escribe el nombre del producto: ")
    try:    
     precio_base: float = float(input("Escribe el precio del producto: "))
     cantidad: int = int(input("Escribe la cantidad que deseas comprar:"))
    except ValueError:
        print("Entrada no válida. Este producto no se añadirá al carrito.")
        continue # Esto hace que el programa vuelva al principio del 'while'
    total_final = calcular_total_item(precio_base, cantidad)

    total_factura += total_final
    producto_completo = {
        "nombre": nombre,
        "precio_total": total_final
    }
    carrito.append(producto_completo)
    continuar = (input("¿Quieres añadir otro producto? (s/n): "))

total_factura = aplicar_descuento(total_factura)

mostrar_ticket(carrito, total_factura)
    
