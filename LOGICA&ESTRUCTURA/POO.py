#¿Qué es la POO y por qué la necesitamos?

"""
Hasta ahora, hemos usado programación estructurada: funciones que manipulan datos sueltos 
(listas, diccionarios).
En la POO, dejamos de pensar en "datos" y empezamos a pensar en "Objetos".
Imagina que un Producto no es solo un nombre y un precio en un diccionario. 
Un Producto es un "ente" que sabe calcular su propio IVA y sabe mostrarse a sí mismo.
"""
#Los dos conceptos clave:
#La Clase: Es el "plano" o "molde" (ej: el plano de un coche).
#El Objeto: Es el producto real construido con ese molde (ej: el coche rojo que tienes en el garaje).

#Clase 10: Nuestra primera Clase

#Vamos a convertir tu diccionario de productos en una Clase. Crea un archivo nuevo llamado poo_productos.py.

"""

class Producto:
    # El "Constructor" (__init__): Se ejecuta al crear el producto
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre        # Atributo
        self.precio = precio        # Atributo
        self.cantidad = cantidad    # Atributo
"""
    # Un "Método": Es una función que el objeto sabe hacer
"""    
    def calcular_total(self):
        total = (self.precio * self.cantidad) * 1.21
        return round(total, 2)
"""        

# --- USANDO LA CLASE ---
# Creamos objetos (instancias)
"""
prod1 = Producto("Laptop", 800, 2)
prod2 = Producto("Mouse", 20, 5)

print(f"Producto: {prod1.nombre}, Total con IVA: ${prod1.calcular_total()}")
print(f"Producto: {prod2.nombre}, Total con IVA: ${prod2.calcular_total()}")
"""
#¿Qué es ese famoso self?
#En Python, self es como decir "yo mismo". Cuando dices self.nombre, el objeto está diciendo
#"mi propio nombre". Es obligatorio ponerlo como primer parámetro en todas las funciones 
#dentro de una clase.

#----Tu Reto Nivel 10: "El Carrito como Objeto"----

#Vamos a llevar tu aplicación al siguiente nivel. 
#En lugar de tener una lista carrito = [] suelta, vamos a crear una clase Carrito.
#Usa la clase Producto que te mostré arriba.
"""
Crea una clase llamada Carrito.
En su __init__, debe tener una lista vacía: self.lista_productos = [].
Crea un método llamado agregar_producto(self, producto) que reciba un objeto de tipo Producto
 y lo meta en la lista.
Crea un método llamado calcular_gran_total(self) que recorra la lista y sume todos los totales.
"""
#Estructura sugerida:
"""
class Producto:
    # (El código de arriba)
   

class Carrito:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        # añade el producto a la lista
    
    def mostrar_resumen(self):
        # imprime los nombres de lo que hay en el carrito
"""
# --- PRUEBA TU CÓDIGO ---
"""
mi_carrito = Carrito()
p1 = Producto("Teclado", 50, 1)
mi_carrito.agregar_producto(p1)
mi_carrito.mostrar_resumen()
"""
#¿Por qué hacemos esto? Porque ahora tu código es mucho más fácil de leer. 
#Ya no dices carrito.append({...}), ahora dices mi_carrito.agregar_producto(p1). 
#¡Es casi como hablar inglés o español!

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total(self):
        total = (self.precio * self.cantidad) * 1.21
        return round(total, 2)
    
class Carrito:
    def __init__(self):
        self.lista_productos=[]

    def agregar_producto(self,producto):
            self.lista_productos.append(producto)
    def calcular_gran_total(self):
            total=0
            for producto in self.lista_productos:
                total+=producto.calcular_total()
            return total
    def mostrar_resumen(self):
            print("En tu carrito hay:")
            for producto in self.lista_productos:
                print(f"-{producto.nombre}")
            

if __name__ == "__main__":

  mi_carrito= Carrito()
  p1=Producto("Teclado",50,1)
  p2=Producto("Mouse",20,2)
  mi_carrito.agregar_producto(p1)
  mi_carrito.agregar_producto(p2)
  mi_carrito.mostrar_resumen()

