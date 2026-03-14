#Clase 6: Funciones (El nivel Oro) 🏆
#Una función es un bloque de código con nombre que puedes "llamar" cuando lo necesites.

#Anatomía de una función:
"""
# Definimos la función

def calcular_iva(precio):
    resultado = precio * 0.21
    return resultado  # 'return' devuelve el valor al programa principal

# Usamos la función
precio_con_iva = calcular_iva(100)

"""
#Tu Reto Nivel 6: "Modularizando la Caja Registradora"
#Vamos a transformar tu programa anterior usando funciones para que sea mucho más profesional.
"""
1.Crea una función llamada calcular_total_item(precio, cantidad) que:
Calcule el subtotal.
Sume el IVA.
Devuelva (return) el resultado final.

2.Crea una función llamada aplicar_descuento(total) que:
Si el total > 2000, reste el 10%.
Devuelva el total actualizado.

3.Crea una función llamada mostrar_ticket(lista_productos, total_final) que:
Tenga el bucle for que imprime los artículos.
Imprima el total final.

"""
#Estructura sugerida para tu archivo:

"""
def calcular_total_item(precio, cantidad):
    # tu lógica aquí
    return ...

def aplicar_descuento(total):
    # tu lógica aquí
    return ...

# --- PROGRAMA PRINCIPAL ---
# Aquí va tu bucle while, pero llamando a las funciones

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
      print(f"----TOTAL FACTURA----: ${round(total_factura,2)}")
    else:
     print(f"Total de la factura: ${round(total_factura,2)}")  
    return total_factura

def mostrar_ticket(lista_productos, total_final):
    print("RESUMEN DE COMPRA:")
    print("-------------------------")
    for producto_completo in lista_productos:
        print(f"- {producto_completo['nombre']}: ${round(producto_completo['precio_total'], 2)}")
    print(f"TOTAL FACTURA: ${round(total_final,2)}")

while continuar == "s":
 nombre: str = input("Escribe el nombre del producto: ")
 precio_base: float = float(input("Escribe el precio del producto: "))
 cantidad: int = int(input("Escribe la cantidad que deseas comprar:"))

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
    
