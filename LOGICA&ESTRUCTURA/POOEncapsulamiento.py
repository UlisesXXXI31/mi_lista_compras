#Clase 12: Encapsulamiento (Protegiendo los datos) 🛡️

#Imagina que alguien, por error, escribe en tu programa: p1.precio = -500. 
# ¡Tu carrito se rompería o el cliente acabaría debiéndote dinero!
#Para evitar esto, usamos el Encapsulamiento. 

# En Python, ponemos un guion bajo _ o dos __ antes del nombre de una variable 
# para indicar que es "privada" y no debería tocarse desde fuera de la clase.

# Ejemplo:

"""
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio  # Variable PRIVADA

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo")
"""

#Tu Reto Nivel 12: "El sistema de seguridad"
#Vamos a aplicar seguridad a nuestra clase Producto.

"""
Cambia los atributos precio y cantidad para que sean privados 

(usa self.__precio y self.__cantidad).

1.Crea un método llamado set_cantidad(self, nueva_cantidad) 
que solo permita cambiar la cantidad si el número es mayor a cero.

2.Modifica el método calcular_total para que use las nuevas variables privadas.

¿Por qué hacemos esto? Porque así aseguras que nadie pueda poner 
"cantidades negativas" o "precios absurdos" desde fuera de tu objeto.

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