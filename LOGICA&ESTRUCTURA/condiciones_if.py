#Ejemplo de condiciones if
"""
total = 1500

if total > 1000:
    print("¡Tienes un descuento del 10%!")
    total = total * 0.90
else:
    print("No hay descuento disponible.")

print(f"Total a pagar: {total}")
"""
#Importante! Fíjate en los dos puntos : al final de la condición y en el espacio 
# (sangría/indentación) a la izquierda. En Python, ese espacio es obligatorio; 
# le dice a la computadora qué líneas de código pertenecen al if.

#Tu Reto Nivel 2: "El Cajero Inteligente"
#Vamos a evolucionar tu programa anterior. Quiero que hagas lo siguiente:

"""
Usa el código que ya tienes de los auriculares inhalambricos.
Si el total_final es mayor a 1000, aplica un descuento del 15% sobre ese total.
Si el total_final es mayor a 500 pero menor o igual a 1000, aplica un descuento del 5%.
Si es menor a 500, no hay descuento.
Muestra el total final después del descuento y cuánto dinero se ahorró el cliente.
Extra: Usa input() para que el usuario pueda escribir el nombre del producto y el precio, 
en lugar de dejarlos fijos en el código. (Recuerda usar float() o int() para convertir 
lo que escriba el usuario).

"""
#**************************************************************#
nombre : str= str(input("Escribe el nombre del producto"))
precio_base: float= float(input("Escribe el precio del producto"))
cantidad : int = int(input("Escribe la cantidad que deseas comprar"))
subtotal= precio_base * cantidad
iva = subtotal * 0.21
total_final =subtotal + iva

if total_final >1000:
    descuento = total_final * 0.15
    total_fial = total_final -descuento
    print(f"Total final después del descuento: ${round(total_final,2)}")
    print(f"Dinero ahorrado: ${round(descuento,2)}")
elif total_final > 500:
    descuento = total_final * 0.05
    total_final =total_final - descuento
    print(f"Total final después del descuento: ${round(total_final,2)}")
    print(f"Dinero ahorrado: ${round(descuento,2)}")
else:
    print("NO hay desceunto disponible")

#***********************************************************************#    

#Código limpio y optimizado:

nombre = input("Escribe el nombre del producto: ") # No hace falta str() delante de input
precio_base = float(input("Escribe el precio: "))
cantidad = int(input("Escribe la cantidad: "))

subtotal = precio_base * cantidad
total_final = subtotal * 1.21 # Una forma rápida de sumar el 21% de IVA
descuento = 0 # Empezamos asumiendo que no hay descuento

# Solo calculamos el valor del descuento
if total_final > 1000:
    descuento = total_final * 0.15
elif total_final > 500:
    descuento = total_final * 0.05

# Aplicamos el descuento una sola vez al final
total_con_descuento = total_final - descuento

# Imprimimos los resultados (una sola vez para todos los casos)
if descuento > 0:
    print(f"¡Felicidades! Tienes un descuento.")
    print(f"Total con descuento: ${round(total_con_descuento, 2)}")
    print(f"Dinero ahorrado: ${round(descuento, 2)}")
else:
    print(f"Total a pagar: ${round(total_final, 2)}")
    print("No hay descuento disponible para esta compra.")
