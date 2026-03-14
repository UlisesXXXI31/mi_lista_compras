#Clase 14: Conectando la Lógica POO con la Interfaz
#Ahora viene lo más divertido: hacer que los botones "hagan algo". Vamos a integrar tus clases Producto y Carrito 
# dentro de este archivo.

#1. Preparación del Carrito
"""Primero, necesitamos crear un objeto mi_carrito fuera de las funciones para que sea global y
 guarde los productos mientras la ventana esté abierta."""

#2. La función agregar()
"""Esta función debe:
Leer los datos de los Entry usando .get().
Crear un objeto Producto.
Meterlo en  mi_carrito.
Escribir el nombre en la zona_texto.
Borrar los campos para el siguiente producto."""

#3. La función finalizar()
"""Esta función debe calcular el total y mostrarlo en la etiqueta.
El Código Integrado (Fase Final)"""
#He corregido los .pack() que faltaban y he añadido la lógica. 
#Fíjate bien en cómo usamos tk.END para escribir en la caja de texto:

import tkinter as tk
from tkinter import messagebox # Para mostrar alertas de error

# --- TUS CLASES (La lógica que ya sabías) ---
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total(self):
        return round((self.precio * self.cantidad) * 1.21, 2)

class Carrito:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def calcular_gran_total(self):
        return sum(p.calcular_total() for p in self.lista_productos)

# --- INSTANCIA GLOBAL DEL CARRITO ---
mi_carrito = Carrito()

# --- FUNCIONES PARA LOS BOTONES ---
def agregar_al_carrito():
    try:
        # 1. Obtener datos de la interfaz
        nombre = entrada_nombre.get()
        precio = float(entrada_precio.get())
        cantidad = int(entrada_cantidad.get())

        if nombre == "": raise ValueError

        # 2. Crear producto y añadir al carrito
        nuevo_p = Producto(nombre, precio, cantidad)
        mi_carrito.agregar_producto(nuevo_p)

        # 3. Actualizar la zona de texto visual
        zona_texto.insert(tk.END, f"- {nombre} (x{cantidad}): ${nuevo_p.calcular_total()}\n")

        # 4. Limpiar campos
        entrada_nombre.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_cantidad.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa datos válidos (Nombre, Precio y Cantidad)")

def finalizar_compra():
    total = mi_carrito.calcular_gran_total()
    etiqueta_total.config(text=f"TOTAL A PAGAR (IVA INCLUIDO): ${total}", fg="green", font=("Arial", 12, "bold"))

#EL bot'on limpiar_Carrito debe poner el total a 0 y limpiar la zona de texto, ademas de vaciar la lista de productos del carrito
def limpiar_carrito():
    zona_texto.delete(1.0, tk.END) # Limpiar la zona de texto
    mi_carrito.lista_productos.clear() # Vaciar la lista de productos
    etiqueta_total.config(text="") # Limpiar el total a pagar

# --- INTERFAZ GRÁFICA ---
ventana = tk.Tk()
ventana.title("Caja Registradora Virtual")
ventana.geometry("400x500")

# Etiquetas y Entradas (Ahora con Pack)
tk.Label(ventana, text="Nombre del producto:").pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Precio del producto:").pack(pady=5)
entrada_precio = tk.Entry(ventana)
entrada_precio.pack()

tk.Label(ventana, text="Cantidad del producto:").pack(pady=5)
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack()

# Botones con sus comandos conectados
boton_agregar = tk.Button(ventana, text="Agregar al carrito", command=agregar_al_carrito, bg="lightblue")
boton_agregar.pack(pady=10)

tk.Label(ventana, text="Productos en el carrito:").pack()
zona_texto = tk.Text(ventana, height=10, width=40)
zona_texto.pack(pady=5)

boton_finalizar = tk.Button(ventana, text="Finalizar compra", command=finalizar_compra, bg="lightgreen")
boton_finalizar.pack(pady=10)

boton_limpiar_Carrito = tk.Button(ventana, text="Limpiar carrito", command=limpiar_carrito, bg="salmon")
boton_limpiar_Carrito.pack(pady=5)

etiqueta_total = tk.Label(ventana, text="")
etiqueta_total.pack(pady=10)

ventana.mainloop()