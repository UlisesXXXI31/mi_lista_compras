#Clase 11: Métodos Especiales (Dándole "superpoderes" a los objetos)
#En Python existen los llamados "Dunder Methods" (Double Underline). 
# Ya conoces __init__, pero hay otro muy importante: __str__.

""""
¿Te has fijado que si haces print(p1) Python te saca algo raro como <__main__.Producto object at 0x000...>?
Si definimos __str__, podemos decirle a Python cómo queremos que se vea el objeto al imprimirlo.
"""

#Ejemplo:

"""
class Producto:
    # ... (tu init anterior) ...
    
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio}"

p1 = Producto("Teclado", 50, 1)
print(p1) # Ahora imprimirá: Producto: Teclado | Precio: $50
"""

#Tu Reto Nivel 11: "La Herencia" (El corazón de la POO) 🧬
#A veces tenemos productos que son especiales. Por ejemplo, productos que están en Oferta. No queremos reescribir toda la clase Producto, queremos una que "herede" todo lo de Producto pero cambie algo.

"""
Crea una clase llamada ProductoOferta que herede de Producto. 
Se hace así: 
class ProductoOferta(Producto):.

Sobrescribe (vuelve a escribir) el método calcular_total.
En esta nueva clase, el método debe aplicar un descuento adicional del 20% 
antes de aplicar el IVA.
En tu código de prueba, añade un producto normal y un ProductoOferta al carrito 
y mira cómo el carrito calcula todo correctamente sin que le importe si son normales 
o de oferta.
¿Por qué es esto importante? Porque el Carrito llamará a .calcular_total() 
y cada objeto sabrá cómo calcularse a sí mismo (esto se llama Polimorfismo).
"""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total(self):
        total = (self.precio * self.cantidad) * 1.21
        return round(total, 2)
    
    # El método __str__ va DENTRO de la clase base
    def __str__(self):
        return f"Producto: {self.nombre} | Precio unitario: ${self.precio} | Cantidad: {self.cantidad}"

class ProductoOferta(Producto):
    def calcular_total(self):
        # Usamos la lógica de descuento
        precio_con_descuento = self.precio * 0.8
        total = (precio_con_descuento * self.cantidad) * 1.21
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