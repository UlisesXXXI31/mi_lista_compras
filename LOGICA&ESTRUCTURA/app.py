#1. Los 4 tipos de datos básicos:


# 1. String (Texto) - Siempre entre comillas
nombre_producto = "Laptop Gamer"

# 2. Integer (Entero) - Números sin decimales
cantidad = 5

# 3. Float (Flotante) - Números con decimales
precio_unitario = 899.99

# 4. Boolean (Booleano) - Solo True o False (Cuidado: la primera letra en Mayúscula)
tiene_descuento = True

# Para saber qué tipo de dato es, usamos la función type()
print(type(nombre_producto))
print(type(precio_unitario))

#2. Operaciones Matemáticas

#Python es una calculadora potente. Prueba estos operadores en tu código:
"""
+ (Suma)
- (Resta)
* (Multiplicación)
/ (División - siempre devuelve un decimal)
// (División entera - quita los decimales)
** (Potencia - ej: 2 ** 3 es 8)
% (Módulo - el resto de una división)
"""
#El Reto de la Clase: "El Gestor de Inventario"
#Para dominar esto, vamos a crear un pequeño programa que gestione el costo de un producto.
#Tu misión: Escribe un código que haga lo siguiente:
"""
Crea una variable para el nombre de un artículo.
Crea una variable para su precio_base (con decimales).
Crea una variable para la cantidad que vas a comprar (entero).
Calcula el Subtotal (precio * cantidad).
Calcula el Impuesto (IVA), que es el 21% del subtotal (multiplica por 0.21).
Calcula el Total Final (Subtotal + IVA).
Muestra en pantalla un mensaje elegante usando f-strings que diga:
"Has comprado [cantidad] unidades de [nombre]. El total con impuestos es: $[total]"
Tip de experto: Recuerda que puedes redondear el resultado final 
usando la función round(valor, 2) para que solo tenga 2 decimales.

"""
nombre : str = "Auriculares Inalámbricos"
precio_base:float = 59.99
cantidad: int = 3
subtotal =precio_base * cantidad
iva = subtotal * 0.21
total = subtotal + iva

print (f"Has comprado {cantidad} unidades de {nombre}.El total com impuestos es:${round(total,2)}")
