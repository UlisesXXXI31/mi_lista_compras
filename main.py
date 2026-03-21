 
#Ahora viene el momento de la verdad: **vamos a generar tu archivo .APK**.

### Paso 1: Asegura el nombre del archivo
#Flet, por defecto, busca un archivo llamado **`main.py`** para empaquetar la aplicación. 
#*   Si tu archivo de la lista de la compra se llama así, perfecto.
#*   Si se llama `lista_compra.py`, cámbiale el nombre a **`main.py`** antes de seguir.

### Paso 2: El comando de construcción (Build)
#Ejecuta este comando en la terminal de VS Code:


#.\.venv\Scripts\flet build apk




### ¿Qué verás en la pantalla? (Ten paciencia ☕)
##Este proceso es como "cocinar" la app y lleva varias etapas:
#1.  **Checking Flutter SDK:** Verificará que todo esté en orden.
#2.  **Copying app project:** Preparará tus archivos.
#3.  **Running 'flutter build apk':** Esta es la parte más larga. Verás que descarga herramientas 
#como **Gradle** y compila el código. Puede tardar de 5 a 10 minutos la primera vez.



### Posibles errores y soluciones rápidas:
#*   **Si te pide "Java":** Android necesita Java para compilar. Si te da un error de `JAVA_HOME`,
 #simplemente abre Android Studio, ve a *Settings > Build, Execution, Deployment > Build Tools > Gradle* 
 #y mira qué versión de JDK está usando. Normalmente, Android Studio ya trae una que podemos usar.
#*   **Si falta el "ndk":** Si te dice que falta el NDK, abre Android Studio -> SDK Manager -> SDK Tools -> 
#marca "NDK (Side by side)" e instala.


### Paso 3: ¿Dónde está mi App?
#Cuando termine (verás un mensaje de éxito), el archivo estará en:
#`C:\Users\Daniel\source\repos\pythonworkspace\app2\build\apk\app-release.apk` 
#(o una ruta similar que te mostrará la consola).

### Paso 4: ¡A tu móvil!
#1.  Copia ese archivo **`.apk`** a tu teléfono.
#2.  Ábrelo e instálalo.
#3.  **¡Disfruta de tu propia creación!**

#**Lanza el comando y dime qué sucede.** Si se queda "congelado" un rato, no te preocupes, 
#está trabajando. Si sale algún error en rojo, pégame las últimas líneas aquí mismo. ¡Estamos en la recta final, desarrollador! 📱🔥


import flet as ft

import traceback

import os

from supabase import create_client
from main_cloud import main as main_func





# 1. CONFIGURACIÓN DE SEGURIDAD (Para Render)

url = os.environ.get("SUPABASE_URL")

key = os.environ.get("SUPABASE_KEY")



supabase = None

try:

    if url and key:

        supabase = create_client(url, key)

except Exception as e:

    print(f"Error conectando a Supabase: {e}")



# --- COMPONENTE VISUAL ---

class ItemCompra(ft.Row):

    """Representa un solo producto en la lista"""

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



# --- FUNCIÓN PRINCIPAL ---

def main(page: ft.Page):

    try:

        page.title = "Mi Lista Pro"

        page.theme_mode = ft.ThemeMode.LIGHT

        page.padding = 20

        

        lista_view = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)



        # Lógica de persistencia local

        def guardar_datos():

            try:

                nombres = [item.nombre for item in lista_view.controls]

                page.client_storage.set("productos", nombres)

            except:

                pass 



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



        # Carga protegida de datos

        try:

            if page.client_storage.contains("productos"):

                datos = page.client_storage.get("productos")

                if datos:

                    for p in datos:

                        lista_view.controls.append(ItemCompra(p, borrar_item))

        except:

            page.client_storage.clear()



        entrada_txt = ft.TextField(

            label="¿Qué necesitas?", 

            expand=True, 

            on_submit=agregar_producto

        )



        page.add(

            ft.Row([

                ft.Text("🛒 Lista", size=30, weight="bold"),

                ft.IconButton(ft.icons.DELETE_SWEEP, icon_color="orange", on_click=limpiar_lista_completa)

            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            ft.Row([entrada_txt], alignment="center"),

            ft.Divider(height=10),

            lista_view

        )



        page.floating_action_button = ft.FloatingActionButton(

            icon=ft.icons.ADD, bgcolor=ft.colors.BLUE_700, on_click=agregar_producto

        )

        page.update()



    except Exception:

        error_txt = traceback.format_exc()

        page.add(ft.Container(

            content=ft.Text(f"ERROR DE ARRANQUE:\n\n{error_txt}", color="white"),

            bgcolor="red", padding=20, expand=True

        ))

        page.update()



# Configuración ultra-compatible para Vercel
app = ft.app(
    target=main_func,
    export_asgi=True
    )
