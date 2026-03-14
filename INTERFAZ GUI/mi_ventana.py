#Fase 3: Interfaces Gráficas (GUI) con Tkinter

#Vamos a dejar de usar la terminal negra y fría para crear una ventana 
# real de Windows/Mac con botones, cajas de texto y etiquetas. 
# Usaremos Tkinter, que ya viene instalado con Python.

#Tu Primera Ventana
#Crea un archivo nuevo llamado mi_ventana.py y escribe esto:

"""
import tkinter as tk

def saludar():
    nombre = entrada.get() # Obtenemos el texto de la caja
    etiqueta_saludo.config(text=f"Hola {nombre}!")

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera App")
ventana.geometry("300x200")

# 2. Crear elementos (Widgets)
etiqueta = tk.Label(ventana, text="Escribe tu nombre:")
etiqueta.pack(pady=10) # pack() coloca el elemento en la ventana

entrada = tk.Entry(ventana) # Caja de texto
entrada.pack()

boton = tk.Button(ventana, text="¡Saludar!", command=saludar)
boton.pack(pady=10)

etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.pack()


# 3. Arrancar la aplicación
ventana.mainloop()
"""
#El Gran Reto de la Fase 3: "La Caja Registradora Visual"
#Tu misión es unir todo lo que has aprendido de POO con esta nueva herramienta visual.
"""
Crea una ventana que tenga campos para escribir Nombre, Precio y Cantidad.
Un botón que diga "Agregar al Carrito".
Cada vez que se pulse el botón, se debe crear un objeto Producto y guardarlo en un objeto Carrito (puedes usar las clases que ya tienes).
Una zona de texto (o una lista visual) donde se vayan mostrando los productos añadidos.
Un botón de "Finalizar Compra" que muestre el total en una etiqueta grande.
"""
""" 
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.__precio = precio  # Variable privada
        self.__cantidad = cantidad  # Variable privada

    #getters y setters para acceder a las variables privadas

    def get_precio(self):
        return self.__precio
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo")
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad > 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa")

    def calcular_total(self):
        total = (self.get_precio() * self.get_cantidad()) * 1.21
        return round(total, 2)
    
    # El método __str__ va DENTRO de la clase base
    def __str__(self):
        return f"Producto: {self.nombre} | Precio unitario: ${self.get_precio()} | Cantidad: {self.get_cantidad()}"

class ProductoOferta(Producto):
    def calcular_total(self):
        # Usamos la lógica de descuento
        precio_con_descuento = self.get_precio() * 0.8
        total = (precio_con_descuento * self.get_cantidad()) * 1.21
        return round(total, 2)

class Carrito:
    def __init__(self):
        self.lista_productos = []

    # Un solo método para todos los tipos de productos
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"✅ Agregado al carrito: {producto.nombre}")

    def calcular_gran_total(self):
        total = 0
        for producto in self.lista_productos:
            # Aquí ocurre la magia: cada producto usa SU PROPIO calcular_total()
            total += producto.calcular_total()
        return round(total, 2)

    def mostrar_resumen(self):
        print("\n--- TU CARRITO DETALLADO ---")
        for producto in self.lista_productos:
            # Llamamos a calcular_total para ver el precio final de cada uno
            print(f"- {producto.nombre}: ${producto.calcular_total()}")
        print(f"TOTAL FINAL A PAGAR: ${self.calcular_gran_total()}")
        print("----------------------------\n")

if __name__ == "__main__":
    mi_carrito = Carrito()
    
    # Creamos un producto normal
    p1 = Producto("Teclado Master", 50, 1)
    
    # Creamos un producto en oferta
    p2 = ProductoOferta("Mouse Gamer", 20, 2)
    
    # Los agregamos usando el MISMO método
    mi_carrito.agregar_producto(p1)
    mi_carrito.agregar_producto(p2)
    
    # Vemos el resumen
    mi_carrito.mostrar_resumen()
"""

import tkinter as tk



# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("caja Registradora virtual")
ventana.geometry("400x400")

# 2. Crear elementos (Widgets)

#Se crea la etiqueta y la caja de texto para el nombre del producto
etiqueta_nombre = tk.Label(ventana, text = "Nombre del producto:")
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

#Se crea la etiqueta y la caja de texto para el precio del producto
etiqueta_producto = tk.Label(ventana, text = "Precio del producto:")
entrada_precio =tk.Entry(ventana)
entrada_precio.pack()

#Secrea la etiqueta y la caja de texto para la cantidad del producto
etiqueta_cantidad = tk.Label(ventana, text = "Cantidad del producto:")
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack()

# Se crea el botón para agregar el producto al carrito
boton_agregar = tk.Button( ventana, text = "Agregar al carrito")
boton_agregar.pack()



# Se crea la zona de texto para mostrar los productos añadidos
zona_texto = tk.Text(ventana, height=10, width=40)
zona_texto.pack()

# Se crea el botón para finalizar la compra
boton_finalizar =tk.Button(ventana, text = "Finalizar compra")
boton_finalizar.pack()

# Se crea la etiqueta para mostrar el total a pagar
etiqueta_total = tk.Label(ventana, text="")
etiqueta_total.pack()

# 3. Arrancar la aplicación
ventana.mainloop()

