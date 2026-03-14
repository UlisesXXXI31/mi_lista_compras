
#Primera App multiplataforma con flet: Una lista de la compra.

#Tu Tarea de Mejora "Pro":

#Quiero que intentes añadir una función de "Limpiar lista completa".

"""Añade un botón en la parte superior (o un IconButton al lado del título) que cuando se presione, 
borre todos los controles de lista_view."""
#¿Cómo se hace?
"""Crea el botón.
Su función debe ser lista_view.controls.clear().
No olvides llamar a page.update()."""



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

    def borrar_item(item):
        lista_view.controls.remove(item)
        page.update()

    def agregar_producto(e):
        if entrada_txt.value:
            # Creamos el nuevo item usando nuestra Clase
            lista_view.controls.append(ItemCompra(entrada_txt.value, borrar_item))
            entrada_txt.value = ""
            entrada_txt.focus()
            page.update()

    entrada_txt = ft.TextField(
        label="¿Qué necesitas comprar?", 
        expand=True, 
        on_submit=agregar_producto
    )
    
    lista_view = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

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