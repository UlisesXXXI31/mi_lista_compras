#Clase 13: El toque "Pythonic" (Decoradores @property)
#Aunque lo que has hecho es correcto y se usa mucho en lenguajes como Java, en Python tenemos una forma más elegante de hacer getters y setters para que el código parezca más natural. Se usan decoradores.


#Mira este pequeño cambio:
"""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio

    @property
    def precio(self):
        # Esto actúa como el GETTER
        return self.__precio

    @precio.setter
    def precio(self, valor):
        # Esto actúa como el SETTER
        if valor > 0:
            self.__precio = valor
        else:
            print("Error: Precio inválido")
"""

# Ahora, en lugar de p1.set_precio(60), puedes hacer:
p1 = Producto("Teclado", 50)
p1.precio = 60  # Internamente llama al @precio.setter
print(p1.precio) # Internamente llama al @property

#Esto no es obligatorio cambiarlo ahora, pero es bueno que lo conozcas 
# porque lo verás en muchos códigos profesionales.