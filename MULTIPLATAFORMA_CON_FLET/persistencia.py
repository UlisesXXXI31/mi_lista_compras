#### ¿Cómo funciona `page.client_storage`?

#Imagina que `client_storage` es un **pequeño archivador** que Flet gestiona en la memoria oculta 
# de tu aplicación. 
"""
*   **Es Local:** Los datos se guardan en el dispositivo donde se ejecuta la app (tu PC ahora, tu móvil después).
*   **Es un Diccionario:** Funciona con **Clave** y **Valor**. Por ejemplo: Clave: `"lista"`, Valor: `["pan", "leche"]`.
*   **Es persistente:** Flet guarda el archivo automáticamente al cerrar y lo lee al abrir.
"""



### Paso a paso para implementarlo tú mismo

"""
Debido a que en la lista tenemos **Objetos** (`ItemCompra`), no podemos guardar el objeto entero (porque tiene botones, lógica, etc.). Lo que haremos será guardar solo los **nombres (texto)** de los productos.

Sigue estos pasos dentro de tu función `main`:
"""

#### 1. Crea la función de guardado

"""
Dentro de `main`, define una función que se encargue de "hacer la foto" a la lista actual y guardarla. 
Ponla justo antes de tus otras funciones:


def guardar_datos():
    # Creamos una lista solo con los nombres (texto) de los productos actuales
    nombres = []
    for item in lista_view.controls:
        nombres.append(item.nombre)
        
"""
    
# Guardamos esa lista de texto en el "archivador" con la clave "productos"
"""page.client_storage.set("productos", nombres)"""


#### 2. Actualiza tus funciones de "Cambio"
"""
Ahora, cada vez que la lista cambie, debemos llamar a `guardar_datos()`. Debes añadir esa línea al final de:
*   La función `agregar_producto`.
*   La función `borrar_item`.
*   La lógica de "Limpiar todo" (el botón de la papelera).

"""

#*Ejemplo en agregar:*

"""
def agregar_producto(e):
    if entrada_txt.value:
        lista_view.controls.append(ItemCompra(entrada_txt.value, borrar_item))
        entrada_txt.value = ""
        entrada_txt.focus()
        guardar_datos() # <--- Llamamos a guardar
        page.update()
"""


#### 3. La lógica de Carga (Al abrir la app)
"""Este es el paso final. Al principio de `main` (después de definir `lista_view` pero antes de `page.add`), 
debemos leer el archivador:"""


# Intentamos obtener la lista guardada
"""lista_guardada = page.client_storage.get("productos")"""

# Si existe (no es None), reconstruimos los objetos ItemCompra
"""
if lista_guardada:
    for nombre_prod in lista_guardada:
        lista_view.controls.append(ItemCompra(nombre_prod, borrar_item))
"""


### Tu misión ahora:
"""
Intenta integrar estos tres pasos en tu código. 
1.  Define `guardar_datos`.
2.  Asegúrate de que `agregar`, `borrar` y `limpiar` llamen a esa función.
3.  Escribe el bloque de "Carga" para que al reiniciar la app, los productos aparezcan mágicamente.

"""
#Prueba de fuego:**
"""
1.  Abre la app.
2.  Añade "Manzanas" y "Queso".
3.  Cierra la app (la ventana de Flet).
4.  Ejecútala de nuevo desde VS Code.
**Si "Manzanas" y "Queso" siguen ahí, ¡habrás dominado la persistencia de datos!**

"""




import flet as ft

class ItemCompra(ft.Row):
    def __init__(self, nombre, eliminar_func):
        super().__init__()
        self.nombre = nombre
        self.eliminar_func = eliminar_func
        
        self.checkbox = ft.Checkbox(on_change=self.status_changed)
        self.texto = ft.Text(value=self.nombre, size=18, expand=True)
        
        # En la 0.25.0 esto funciona perfecto y sin cuadros rojos
        self.boton_borrar = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINE,
            icon_color=ft.colors.RED_700,
            on_click=lambda _: self.eliminar_func(self)
        )

        self.controls = [self.checkbox, self.texto, self.boton_borrar]
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

    

    def status_changed(self, e):
        if self.checkbox.value:
            self.texto.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
            self.texto.color = ft.colors.GREY_500
        else:
            self.texto.style = None
            self.texto.color = ft.colors.BLACK
        self.update()

def main(page: ft.Page):
    page.title = "Lista de Compra Estable (v0.25)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 600
    page.padding = 20

    def guardar_datos():
    # Creamos una lista solo con los nombres (texto) de los productos actuales
      nombres = []
      for item in lista_view.controls:
        nombres.append(item.nombre)
    # Guardamos esa lista de texto en el "archivador" con la clave "productos"
      page.client_storage.set("productos", nombres)


    def borrar_item(item):
        lista_view.controls.remove(item)
        guardar_datos() # <--- Llamamos a guardar
        page.update()

    def agregar_producto(e):
     if entrada_txt.value:
        lista_view.controls.append(ItemCompra(entrada_txt.value, borrar_item))
        entrada_txt.value = ""
        entrada_txt.focus()
        guardar_datos() # <--- Llamamos a guardar
        page.update()

    def limpiar_lista_completa(e):
        lista_view.controls.clear()
        guardar_datos() # guardamos que la lista está vacía
        page.update()

    entrada_txt = ft.TextField(
        label="¿Qué necesitas comprar?", 
        expand=True, 
        on_submit=agregar_producto
    )
    
    lista_view = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    # Intentamos obtener la lista guardada
    lista_guardada = page.client_storage.get("productos")
    # Si existe (no es None), reconstruimos los objetos ItemCompra
    if lista_guardada:
        for nombre_prod in lista_guardada:
            lista_view.controls.append(ItemCompra(nombre_prod, borrar_item))

    page.add(
        ft.Row(
            [
                ft.Text("🛒 Lista", size=32, weight="bold"),
                ft.IconButton(
                    icon=ft.icons.DELETE_SWEEP, 
                    icon_color=ft.colors.ORANGE_700,
                    on_click=lambda _: (lista_view.controls.clear(), page.update())
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        ft.Row([entrada_txt], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20),
        lista_view
    )

    # El botón flotante que en 0.25.0 NO da error visual
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.BLUE_700,
        on_click=agregar_producto
    )
    
    page.update()

if __name__ == "__main__":
    # Importante: en 0.25.0 usamos target=main
    ft.app(target=main)

