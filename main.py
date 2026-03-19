 
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
from supabase import create_client, Client

# --- 1. CONFIGURACIÓN DE SEGURIDAD (Vercel lee estas variables) ---
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Inicializamos la variable supabase como None y la cargamos de forma segura
supabase_client: Client = None

try:
    if url and key:
        supabase_client = create_client(url, key)
    else:
        print("ADVERTENCIA: Faltan variables de entorno SUPABASE_URL o SUPABASE_KEY")
except Exception as e:
    print(f"Error conectando a Supabase durante la inicialización: {e}")

# Nombre de la tabla que crearemos en Supabase
TABLA_SUPABASE = "productos_lista"


# --- COMPONENTE VISUAL (Se mantiene casi igual) ---
class ItemCompra(ft.Row):
    """Representa un solo producto en la lista"""
    def __init__(self, nombre, id_supabase, eliminar_func):
        super().__init__()
        # Ahora necesitamos el id_supabase para saber qué borrar en la DB
        self.id_supabase = id_supabase 
        self.nombre = nombre
        self.eliminar_func = eliminar_func
        
        self.checkbox = ft.Checkbox(on_change=self.status_changed)
        self.texto = ft.Text(value=self.nombre, size=18, expand=True)
        self.boton_borrar = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINE,
            icon_color=ft.colors.RED_700,
            on_click=lambda _: self.eliminar_func(self) # Pasa el objeto completo
        )

        self.controls = [self.checkbox, self.texto, self.boton_borrar]
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

    def status_changed(self, e):
        # Esta lógica es solo visual y se mantiene local
        if self.checkbox.value:
            self.texto.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
            self.texto.color = ft.colors.GREY_500
        else:
            self.texto.style = None
            self.texto.color = ft.colors.BLACK
        self.update()


# --- FUNCIÓN PRINCIPAL CON LÓGICA DE CLOUD ---
def main(page: ft.Page):
    try:
        page.title = "Mi Lista Pro 2.0 (Supabase)"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 20
        
        # Vista de la lista (Columna con scroll)
        lista_view = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)
        
        # Diálogo de Carga/Error (Feedback visual para el usuario)
        loading_dialog = ft.AlertDialog(
            content=ft.Row([ft.ProgressRing(), ft.Text(" Sincronizando...")])
        )

        # Helper para verificar si Supabase está disponible
        def supabase_not_ready():
            if not supabase_client:
                page.snack_bar = ft.SnackBar(ft.Text("Supabase no está configurado!"))
                page.snack_bar.open = True
                page.update()
                return True
            return False

        # --- LÓGICA DE PERSISTENCIA EN SUPABASE ---

        def cargar_datos_supabase():
            if supabase_not_ready(): return
            
            # Mostramos loading
            page.dialog = loading_dialog
            loading_dialog.open = True
            page.update()
            
            try:
                # Realizamos un select de todos los productos (ordenados por fecha)
                response = supabase_client.table(TABLA_SUPABASE)\
                                         .select("*")\
                                         .order("created_at", descending=False)\
                                         .execute()
                
                # Limpiamos la vista actual
                lista_view.controls.clear()
                
                # Llenamos la vista con los datos de Supabase
                for row in response.data:
                    # Usamos ItemCompra con id y nombre de la DB
                    lista_view.controls.append(
                        ItemCompra(
                            nombre=row["nombre"],
                            id_supabase=row["id"], # Guardamos el ID de la DB
                            eliminar_func=borrar_item_supabase
                        )
                    )
            except Exception as e:
                print(f"Error cargando datos: {e}")
                # Si falla Supabase, podrías cargar una copia del local_storage aquí
                page.snack_bar = ft.SnackBar(ft.Text(f"Error cargando desde la nube: {e}"))
                page.snack_bar.open = True
                
            # Ocultamos loading
            loading_dialog.open = False
            page.update()

        def agregar_producto_supabase(e):
            if supabase_not_ready() or not entrada_txt.value: return
            
            nombre_producto = entrada_txt.value
            
            try:
                # 1. Insertamos en Supabase
                response = supabase_client.table(TABLA_SUPABASE)\
                                         .insert({"nombre": nombre_producto})\
                                         .execute()
                
                # 2. Obtenemos el ID generado por la DB
                id_generado = response.data[0]["id"]
                
                # 3. Actualizamos la UI localmente (más rápido)
                lista_view.controls.append(
                    ItemCompra(
                        nombre=nombre_producto,
                        id_supabase=id_generado,
                        eliminar_func=borrar_item_supabase
                    )
                )
                
                # Limpiamos el input
                entrada_txt.value = ""
                entrada_txt.focus()
                
                # Sincronizamos con el client_storage como backup local opcional
                # (Omitido aquí para simplificar, confiaremos en Supabase)
                
            except Exception as e:
                print(f"Error insertando datos: {e}")
                page.snack_bar = ft.SnackBar(ft.Text(f"No se pudo guardar: {e}"))
                page.snack_bar.open = True
            
            page.update()

        def borrar_item_supabase(item):
            """Elimina un producto de la nube y de la UI"""
            if supabase_not_ready(): return
            
            try:
                # 1. Eliminamos de Supabase usando el ID que guardamos
                supabase_client.table(TABLA_SUPABASE)\
                                .delete()\
                                .eq("id", item.id_supabase)\
                                .execute()
                
                # 2. Eliminamos de la UI localmente
                lista_view.controls.remove(item)
                
            except Exception as e:
                print(f"Error borrando datos: {e}")
                page.snack_bar = ft.SnackBar(ft.Text(f"Error borrando: {e}"))
                page.snack_bar.open = True
                
            page.update()

        def limpiar_lista_completa_supabase(e):
            """Lógica peligrosa: borra todo de Supabase"""
            if supabase_not_ready(): return
            
            try:
                # En Supabase (con RLS desactivado o configurado para borrar)
                # una forma sencilla de borrar "todo" es seleccionar todos los ids y borrarlos
                # o usar una API Key de service_role. 
                # Para evitar problemas de permisos, haremos un borrado iterativo simple:
                
                if lista_view.controls:
                    page.dialog = loading_dialog
                    loading_dialog.open = True
                    page.update()
                    
                    ids_a_borrar = [item.id_supabase for item in lista_view.controls]
                    # Borrado masivo por ID
                    supabase_client.table(TABLA_SUPABASE)\
                                   .delete()\
                                   .in_("id", ids_a_borrar)\
                                   .execute()
                                   
                    lista_view.controls.clear()
            except Exception as e:
                print(f"Error limpiando lista: {e}")
                page.snack_bar = ft.SnackBar(ft.Text(f"Error: {e}"))
                page.snack_bar.open = True

            loading_dialog.open = False
            page.update()


        # --- COMPONENTES DE UI ---

        entrada_txt = ft.TextField(
            label="¿Qué necesitas?", 
            expand=True, 
            on_submit=agregar_producto_supabase
        )

        page.add(
            ft.Row([
                ft.Text("🛒 Lista Cloud", size=30, weight="bold"),
                ft.IconButton(ft.icons.DELETE_SWEEP, icon_color="orange", on_click=limpiar_lista_completa_supabase)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([entrada_txt], alignment="center"),
            ft.Divider(height=10),
            lista_view
        )

        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, bgcolor=ft.colors.BLUE_700, on_click=agregar_producto_supabase
        )
        
        # --- ARRANQUE DE LA APP ---
        # Una vez que la UI está montada, cargamos los datos reales
        page.update()
        if supabase_client:
            cargar_datos_supabase()

    except Exception:
        error_txt = traceback.format_exc()
        # Mostramos una pantalla de error visual si algo falla gravemente
        try:
            page.add(ft.Container(
                content=ft.Text(f"ERROR DE ARRANQUE CRÍTICO:\n\n{error_txt}", color="white", font_family="monospace"),
                bgcolor="red_700", padding=20, expand=True, border_radius=10
            ))
            page.update()
        except:
            # Si el error es tan grave que no podemos ni page.add, imprimimos a consola
            print(error_txt)


# --- 2. CONFIGURACIÓN CRÍTICA PARA VERCEL (ASGI) ---
# Exportamos la app como ASGI para que Vercel @vercel/python la maneje
app = ft.app(target=main, export_asgi=True)
