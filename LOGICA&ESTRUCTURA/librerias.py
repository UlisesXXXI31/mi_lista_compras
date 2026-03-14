#Clase 9: Librerías y el Estándar Profesional
#Para que tu aplicación pase de "ejercicio de curso" a "software profesional", 
# vamos a introducir dos conceptos que usan los expertos:

#1. Uso de Librerías (El módulo datetime)

#Las facturas reales tienen fecha y hora. Python viene con "cajas de herramientas" 
# listas para usar llamadas módulos.

"""
import datetime

ahora = datetime.datetime.now()
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha de emisión: {fecha_formateada}")

"""

#2. El "Main Guard" (if __name__ == "__main__":)

"""
En Python profesional, el código que ejecuta el programa no se deja "suelto". 
Se mete dentro de una función principal llamada main(). 
Esto evita que el código se ejecute solo si alguna vez decides importar tus funciones 
desde otro archivo.
"""
#Tu Reto Nivel 9: "La Versión Final Profesional"

"""
Importa datetime al principio del archivo.
Modifica mostrar_ticket y guardar_factura para que incluyan la fecha y hora actual en la cabecera.
Encapsula el bucle principal: Crea una función llamada def menu_principal(): y mete todo tu código del while y las llamadas finales ahí.
"""

#Al final del archivo, añade el estándar profesional:

"""
if __name__ == "__main__":
    menu_principal()
"""

#Extra (Dificultad Pro): Haz que el nombre del archivo incluya la fecha 
# para que no se sobreescriba siempre el mismo. Ejemplo: factura_20_02_2024.txt.

import datetime



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
    ahora = datetime.datetime.now()
    fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Fecha de emisión: {fecha_formateada}")
    print("RESUMEN DE COMPRA:")
    print("-------------------------")
    for producto_completo in lista_productos:
        print(f"- {producto_completo['nombre']}: ${round(producto_completo['precio_total'], 2)}")
    print(f"TOTAL FACTURA: ${round(total_final,2)}")

def guardar_factura(lista_productos, total):
    ahora = datetime.datetime.now()
    fecha_formateada = ahora.strftime("%d_%m_%Y")
    nombre_archivo = f"factura_{fecha_formateada}.txt"
    with open(nombre_archivo, "w") as f:
        f.write(f"Fecha de emisión: {fecha_formateada}\n")
        f.write("RESUMEN DE COMPRA:\n")
        f.write("-------------------------\n")
        for producto_completo in lista_productos:
            f.write(f"- {producto_completo['nombre']}: ${round(producto_completo['precio_total'], 2)}\n")
        f.write(f"TOTAL FACTURA: ${round(total,2)}\n")

def menu_principal():
        
        continuar = "s"
        total_factura = 0
        #1. Se crea la lista carrito vacia para almacenar los nombres de los productos comprados.
        carrito =[]

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

        if carrito: # Solo si hay productos
             total_factura = aplicar_descuento(total_factura)

             mostrar_ticket(carrito, total_factura)

             guardar_factura(carrito, total_factura)
        else:
            print("No se añadieron productos al carrito. No se generará factura.")

if __name__ == "__main__":
    menu_principal()
    