#Clase 8: Persistencia de Datos (Guardar en Archivos)
#Hasta ahora, cada vez que cierras VS Code, tus ventas desaparecen. Un desarrollador experto sabe que los datos deben guardarse. Vamos a aprender a escribir un archivo de texto (.txt) con el resumen de la venta.
#Para manejar archivos en Python usamos open().

#Ejemplo rápido:

# 'w' significa Write (Escribir). Si el archivo no existe, lo crea.
"""
with open("resumen_venta.txt", "w") as archivo:
    archivo.write("Este es el resumen de tu compra\n")
    archivo.write("Gracias por visitarnos.")

"""

#Tu Reto Nivel 8: "El Generador de Facturas"
#Tu aplicación ahora debe guardar el ticket en un archivo físico en tu computadora.
"""
Crea una nueva función llamada guardar_factura(lista_productos, total).
Dentro de la función, usa with open("factura.txt", "w") as f:.
Escribe en el archivo el nombre de cada producto y su precio (usa un bucle for dentro de la función).
Al final del archivo, escribe el Total Final.
Llama a esta función al final de tu programa principal.
"""

#Pista: Para escribir una variable en un archivo, debes convertirla a texto o usar f-strings:
#f.write(f"Producto: {item['nombre']} \n")

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

def guardar_factura(lista_productos, total):
    with open("factura.txt", "w") as f:
        f.write("RESUMEN DE COMPRA:\n")
        f.write("-------------------------\n")
        for producto_completo in lista_productos:
            f.write(f"- {producto_completo['nombre']}: ${round(producto_completo['precio_total'], 2)}\n")
        f.write(f"TOTAL FACTURA: ${round(total,2)}\n")

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

guardar_factura(carrito, total_factura)
    
