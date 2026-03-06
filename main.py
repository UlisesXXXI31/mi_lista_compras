"""
Ahora viene el momento de la verdad: **vamos a generar tu archivo .APK**.

### Paso 1: Asegura el nombre del archivo
Flet, por defecto, busca un archivo llamado **`main.py`** para empaquetar la aplicación. 
*   Si tu archivo de la lista de la compra se llama así, perfecto.
*   Si se llama `lista_compra.py`, cámbiale el nombre a **`main.py`** antes de seguir.

### Paso 2: El comando de construcción (Build)
Ejecuta este comando en la terminal de VS Code:

```powershell
.\.venv\Scripts\flet build apk
```

---

### ¿Qué verás en la pantalla? (Ten paciencia ☕)
Este proceso es como "cocinar" la app y lleva varias etapas:
1.  **Checking Flutter SDK:** Verificará que todo esté en orden.
2.  **Copying app project:** Preparará tus archivos.
3.  **Running 'flutter build apk':** Esta es la parte más larga. Verás que descarga herramientas 
como **Gradle** y compila el código. Puede tardar de 5 a 10 minutos la primera vez.

---

### Posibles errores y soluciones rápidas:
*   **Si te pide "Java":** Android necesita Java para compilar. Si te da un error de `JAVA_HOME`,
 simplemente abre Android Studio, ve a *Settings > Build, Execution, Deployment > Build Tools > Gradle* 
 y mira qué versión de JDK está usando. Normalmente, Android Studio ya trae una que podemos usar.
*   **Si falta el "ndk":** Si te dice que falta el NDK, abre Android Studio -> SDK Manager -> SDK Tools -> 
marca "NDK (Side by side)" e instala.

---

### Paso 3: ¿Dónde está mi App?
Cuando termine (verás un mensaje de éxito), el archivo estará en:
`C:\Users\Daniel\source\repos\pythonworkspace\app2\build\apk\app-release.apk` 
(o una ruta similar que te mostrará la consola).

### Paso 4: ¡A tu móvil!
1.  Copia ese archivo **`.apk`** a tu teléfono.
2.  Ábrelo e instálalo.
3.  **¡Disfruta de tu propia creación!**

**Lanza el comando y dime qué sucede.** Si se queda "congelado" un rato, no te preocupes, 
está trabajando. Si sale algún error en rojo, pégame las últimas líneas aquí mismo. ¡Estamos en la recta final, desarrollador! 📱🔥
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

import flet as ft

class ItemCompra(ft.Row):
    def __init__(self, nombre, eliminar_func):
        super().__init__()
        self.nombre = nombre
        self.eliminar_func = eliminar_func
        
        self.checkbox = ft.Checkbox(on_change=self.status_changed)
        self.texto = ft.Text(value=self.nombre, size=18, expand=True)
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
    # 1. AJUSTES DE SEGURIDAD PARA MÓVIL
    page.title = "Mi Lista"
    page.theme_mode = ft.ThemeMode.LIGHT
    # En móvil no fijamos ancho/alto, dejamos que se adapte solo
    
    lista_view = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    def guardar_datos():
        try:
            nombres = [item.nombre for item in lista_view.controls]
            page.client_storage.set("productos", nombres)
        except Exception as ex:
            print(f"Error al guardar: {ex}")

    def borrar_item(item):
        lista_view.controls.remove(item)
        guardar_datos()
        page.update()

    def agregar_producto(e):
        if entrada_txt.value:
            lista_view.controls.append(ItemCompra(entrada_txt.value, borrar_item))
            entrada_txt.value = ""
            entrada_txt.focus()
            guardar_datos()
            page.update()

    def limpiar_lista_completa(e):
        lista_view.controls.clear()
        guardar_datos()
        page.update()

    # 2. CARGA DE DATOS PROTEGIDA (El posible culpable del cierre)
    try:
        if page.client_storage.contains("productos"):
            lista_guardada = page.client_storage.get("productos")
            if lista_guardada and isinstance(lista_guardada, list):
                for nombre_prod in lista_guardada:
                    lista_view.controls.append(ItemCompra(nombre_prod, borrar_item))
    except Exception:
        # Si falla la carga, limpiamos el storage para que la app no muera
        page.client_storage.clear()

    entrada_txt = ft.TextField(
        label="¿Qué necesitas?", 
        expand=True, 
        on_submit=agregar_producto
    )

    page.add(
        ft.Row(
            [
                ft.Text("🛒 Lista", size=30, weight="bold"),
                ft.IconButton(
                    icon=ft.icons.DELETE_SWEEP, 
                    icon_color=ft.colors.ORANGE_700,
                    on_click=limpiar_lista_completa
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        ft.Row([entrada_txt], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=10),
        lista_view
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.BLUE_700,
        on_click=agregar_producto
    )
    
    page.update()

if __name__ == "__main__":
    # Importante: No uses la ruta completa del archivo aquí
    ft.app(target=main)