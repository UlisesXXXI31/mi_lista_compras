#Para probar si la conexión funciona, vamos a crear una interfaz rápida. Crea un archivo llamado `main_cloud.py`:





import flet as ft
from supabase_manager import CloudManager
from finanzas import VistaFinanzas
# --- CLASE: REPRESENTA CADA PRODUCTO ---
class ItemCompraCloud(ft.Card): # Ahora heredamos de Card para tener elevación:
    def __init__(self, db_id, nombre, precio, completado, eliminar_func):
        super().__init__()
        self.db_id = db_id
        self.nombre = nombre
        self.precio = precio
        self.eliminar_func = eliminar_func # Guardamos la referencia a la función de borrado

        # Diseño interno del ítem
        self.content = ft.Container(
            padding=10,
            content=ft.ListTile(
                leading=ft.Checkbox(
                    value=completado,
                    fill_color=ft.Colors.GREEN_400, # Color del check
                    on_change=lambda e: self.cambiar_estado(e)
                ),
                title=ft.Text(
                    f"{self.nombre}",
                    size=18,
                    weight="bold",
                    # Si ya está completado, sale tachado de inicio
                    style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH if completado else None)
                ),
                  subtitle=ft.Text(f"$ {self.precio:.2f}", color=ft.Colors.BLUE_GREY_400),
                  trailing=ft.IconButton(
                    icon=ft.Icons.DELETE_SWEEP_ROUNDED,
                    icon_color=ft.Colors.RED_400,
                    on_click=self.preparar_borrado
                ),
            )
        )
        self.elevation = 2 # Sombra sutil
        self.margin = 5        
                
        self.leading = ft.Checkbox(
        value=completado, 
        on_change=lambda e: CloudManager.actualizar_estado_db(self.db_id, e.control.value)
        )
        
    def cambiar_estado(self, e):
        # Efecto visual dinámico al marcar/desmarcar
        self.content.content.title.style.decoration = (
            ft.TextDecoration.LINE_THROUGH if e.control.value else None
        )
        self.content.content.title.color = ft.Colors.GREY_500 if e.control.value else ft.Colors.BLACK
        CloudManager.actualizar_estado_db(self.db_id, e.control.value)
        self.update()

    def preparar_borrado(self, e):
        e.control.disabled = True # Evita doble clic
        self.update() 
        self.eliminar_func(self) # Le pide a la lista principal que lo borre

# --- FUNCIÓN PRINCIPAL DE LA APP ---
def main(page: ft.Page):
    page.title = "Asistente de Compras Cloud"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    # Texto del total (se crea fuera para que sea persistente)
    total_text = ft.Text(value="Total: $0.00", size=28, weight="bold", color=ft.Colors.GREEN_700)

    def mostrar_asistente(user_id):
        page.clean()
        page.bgcolor = ft.Colors.GREY_50 # Fondo gris muy clarito

         # 1. DEFINIMOS LAS PIEZAS PRIMERO (Los "Músculos")
         # ------------------------------------------------ #
       
        # La etiqueta del dinero (IMPORTANTE: Se crea aquí una sola vez)
        total_label = ft.Text("$ 0.00", size=36, weight="bold", color=ft.Colors.BLUE_900)

         # Campos de entrada con diseño redondeado y bordes suaves
        txt_nombre = ft.TextField(
        label="¿Qué vas a comprar?",
        border_radius=15,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
        bgcolor=ft.Colors.WHITE,
        expand=True
        )

        txt_precio = ft.TextField(
        label="Precio",
        width=100,
        border_radius=15,
        keyboard_type="number",
        prefix_text="€", 
        bgcolor=ft.Colors.WHITE
        )

        sel_cat = ft.Dropdown(
        label="Cat.", width=120,
        options=[ft.dropdown.Option("Comida"), ft.dropdown.Option("Hogar"), ft.dropdown.Option("Otros")],
        value="Comida"
        )

        # La lista donde se verán los productos
        lista_view = ft.ListView(expand=True, spacing=10, padding=10)

        
         # --- 2. DEFINIMOS EL "CEREBRO" (LÓGICA) ---
         # Lógica: Suma todos los precios de los productos en pantalla

        def calcular_total():
            suma = 0
            for item in lista_view.controls:
                if isinstance(item, ItemCompraCloud):
                    suma += item.precio
            total_label.value = f"Total: €{suma:.2f}"
            page.update()

        # Lógica: Borrar en Nube y luego en Pantalla
        def borrar_item_cloud(item_ui):
            # 1. Borramos en Supabase usando el ID (número)
            CloudManager.borrar_producto_db(item_ui.db_id)
            
            # 2. Borramos de la lista visual usando el OBJETO
            if item_ui in lista_view.controls:
                lista_view.controls.remove(item_ui)
                calcular_total() # Refrescamos el dinero total

        # Lógica: Agregar nuevo producto
        def agregar_click(e):
            if txt_nombre.value and txt_precio.value:
                try:
                    precio_num = float(txt_precio.value)
                    # Guardamos en Supabase
                    nuevo = CloudManager.agregar_producto_db(user_id, txt_nombre.value, precio_num, sel_cat.value)
                    if nuevo:
                        lista_view.controls.append(
                            ItemCompraCloud(nuevo['id'], nuevo['nombre'], nuevo['precio'], False, borrar_item_cloud)
                        )
                        txt_nombre.value = ""
                        txt_precio.value = ""

                        calcular_total()
                        page.update()

                        txt_nombre.focus()
                        page.update()
                        
                except ValueError:
                    page.snack_bar = ft.SnackBar(ft.Text("⚠️ Precio no válido"), bgcolor="red")
                    page.snack_bar.open = True
                    page.update()

                
        # Botón de añadir Estilo "Pill"
        btn_add = ft.FloatingActionButton(
            content=ft.Row([ft.Icon(ft.Icons.ADD), ft.Text("Añadir")], alignment="center"),
            width=120,
            shape=ft.RoundedRectangleBorder(radius=15),
            bgcolor=ft.Colors.BLUE_600,
            on_click=agregar_click # Tu función actual
        )

        # AQUÍ DEFINIMOS total_container (La pieza que te faltaba)
        total_container = ft.Container(
        content=ft.Column([
            ft.Text("GASTO TOTAL ESTIMADO", size=12, weight="bold", color=ft.Colors.BLUE_GREY_400),
            total_label
        ], horizontal_alignment="center"),
        bgcolor=ft.Colors.WHITE,
        padding=30,
        border_radius=25,
        shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.BLUE_GREY_100)
       )

        
        
          # 3. DEFINIMOS LOS CONTENEDORES DE VISTA (El "Escenario")
          # ------------------------------------------------------

        contenedor_lista = ft.Column(visible=True,expand=True) # Visible al inicio
        contenedor_finanzas = ft.Column(visible=False,expand=True) # Oculto al inicio


        #4. CARGAMOS LOS DATOS DESDE LA NUBE (El "Archivo de Datos")
        
        productos_db = CloudManager.obtener_productos_db(user_id)
        for p in productos_db:
            # Manejo de nulos para evitar errores de formateo
            precio_real = p['precio'] if p['precio'] is not None else 0.0
            lista_view.controls.append(
                ItemCompraCloud(p['id'], p['nombre'], precio_real, p['completado'], borrar_item_cloud)
            )

          # 4. ARMAMOS EL DISEÑO DE LA LISTA
          # --------------------------------
          # Ahora que las piezas existen, podemos meterlas en el contenedor

        contenedor_lista.controls = [
        # Cabecera
        ft.Container(
            content=ft.Column([
                ft.Text("BALANCE DE COMPRA", size=12, weight="bold", color=ft.Colors.BLUE_GREY_400),
                total_label
            ], horizontal_alignment="center"),
            padding=20, bgcolor=ft.Colors.WHITE, border_radius=25,
        ),
        ft.Divider(height=20, color="transparent"),
        # Fila de entrada
        ft.Row([txt_nombre, txt_precio], spacing=10),
        ft.Row([sel_cat], alignment="end"),
        ft.Divider(height=10, color="transparent"),
        # La lista de productos
        ft.Text("  MI CARRITO", size=16, weight="bold", color=ft.Colors.BLUE_GREY_700),
        lista_view
        ]

        
        # 5. ARMAMOS EL DISEÑO DE FINANZAS (Vacío por ahora)
        # -------------------------------------------------
        contenedor_finanzas.controls = [
        ft.Container(
        content=ft.Text("📊 PANEL DE GASTOS", size=24, weight="bold"),
        padding=50, alignment=ft.alignment.center
        ),
        ]

        contenedor_finanzas= VistaFinanzas(user_id)
       # 6. LA LÓGICA DE NAVEGACIÓN
       # --------------------------
    
        def cambiar_tab(e):
         idx = e.control.selected_index
         contenedor_lista.visible = (idx == 0)
         contenedor_finanzas.visible = (idx == 1)
         page.update()

         #El btn_add debe ser visible solo en pantalla lista
         btn_add.visible = (idx==0)

         if idx==1:
            contenedor_finanzas.cargar_datos

            page.update()
         


        # La barra de navegación profesional
        page.navigation_bar = ft.NavigationBar(
        destinations=[
            # Cambiamos NavigationDestination por NavigationBarDestination
            ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART, label="Lista"),
            ft.NavigationBarDestination(icon=ft.Icons.MONETIZATION_ON, label="Gastos"),
        ],
        on_change=cambiar_tab
         )
        # 7. LANZAMOS TODO AL ESCENARIO
        # -----------------------------
        page.floating_action_button = btn_add
        page.add(contenedor_lista, contenedor_finanzas)
        page.update()


    # --- INICIO (LOGIN) ---
    email_input = ft.TextField(label="Email", border_radius=10)
    pass_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    
    def login_click(e):
        uid = CloudManager.login_usuario(email_input.value, pass_input.value)
        if uid:
            mostrar_asistente(uid)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("❌ Login incorrecto"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        ft.Icon(ft.Icons.CLOUD_DONE, size=60, color="blue"),
        ft.Text("Asistente Cloud Login", size=24, weight="bold"),
        email_input, 
        pass_input, 
        ft.ElevatedButton("Iniciar Sesión", on_click=login_click, width=250)
    )

if __name__ == "__main__":
    ft.app(target=main)
