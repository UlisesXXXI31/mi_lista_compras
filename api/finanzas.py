#Creamos la clase VistaFinanzas que contenga user_id
""" Debe tener:
1.  Un **`__init__`** que reciba el `user_id`.
2.  Un componente **`ft.PieChart`** (aunque esté vacío por ahora).
3.  Un **`ft.TextField`** para que el usuario escriba su presupuesto (ej: "300").
4.  Un **`ft.ElevatedButton`** que llame a tu nueva función `actualizar_presupuesto`."""

import flet as ft
from supabase_manager import CloudManager

class VistaFinanzas(ft.Column):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.expand=True
        self.scroll= "adaptive"

        #Elemento de la grafica (vacio al inicio)
         
        self.grafica = ft.PieChart(
            sections=[],
            sections_space=2,
            center_space_radius=40,
            height=250, # <--- DALE UNA ALTURA FIJA PARA PROBAR
            expand=False # <--- Ponlo en False momentáneamente
        )
        self.txt_resumen= ft.Text("Distribucion de Gastos",
                                  size=16, 
                                  weight="bold")
        #Input para presupuesto
        self.txt_presupuesto= ft.TextField(label="Presupuesto mensual", 
                                           width=200,
                                           suffix="€",
                                           keyboard_type="number")
        #Boton para actualizar presupuesto
        self.btn_actualizar= ft.ElevatedButton("Actualizar Presupuesto",
                                               icon =ft.Icons.SAVE, 
                                               on_click=self.on_click_actualizar)

        #Asignacion a la pantalla
        #Esto es lo que dibuja los elementos e la columna

        self.controls = [
            ft.Text("📊 MI ANALISTA", size=25, weight="bold"),
            ft.Container(
                content=self.grafica, 
                padding=20, 
                bgcolor=ft.Colors.BLUE_GREY_50, # Color de fondo para ver el área
                border_radius=20,
                height=300 # Altura del contenedor
            ),
            self.txt_resumen,
            ]
        #Al iniciar la vista, cargamos el presupuesto actual del usuario para mostrarlo en el input
        self.txt_presupuesto.value = str(CloudManager.obtener_presupuesto(self.user_id))    
 
        #LOGiCA DE EVENTOS
    
    def on_click_actualizar(self, e):
        """Actualiza el presupuesto en la nube"""
        if self.txt_presupuesto.value:
            try:
                nuevo_monto=float(self.txt_presupuesto.value)
                #Llamamos a la funcion de Supabase para actualizar el presupuesto
                exito=CloudManager.actualizar_presupuesto(self.user_id, nuevo_monto)
                if exito:
                    self.txt_presupuesto.error_text= None
                    #Mostramos un aviso de exito
                    e.page.snack_bar=ft.SnackBar(ft.Text("✅Presupuesto guardado en la nube"))
                    e.page.snack_bar=True
                else:
                    e.page.snack_bar=(ft.SnackBar("❌ Error al conectar con Supabase"))
                    
                    e.page.snack_bar.open=True
            except ValueError:
                self.txt_presupuesto.error_text= "Ingrese un numero valido"
                self.update()

    #Añade un método llamado `cargar_datos(self)` 
    # dentro de la clase `VistaFinanzas`.
    """Este método debe:
    1. Llamar a `CloudManager.obtener_resumen_gastos(self.user_id)` (la función que suma categorías que planeamos antes).
    2. Crear una lista de `ft.PieChartSection` con esos datos.
    3. Asignar esa lista a `self.grafica.sections`."""
    def cargar_datos(self):
        """Carga los datos almacenados en la nube y refresca la gráfica"""
        resumen_gastos = CloudManager.obtener_resumen_gastos(self.user_id)
        
         # --- LÍNEA DE DEBUG (Añade esto) ---
        print(f"DEBUG: Datos recibidos de la nube: {resumen_gastos}")
        # -----------------------------------

        if not resumen_gastos:
            self.txt_resumen.value = "DEBUG: No hay datos completados en la DB"
            self.update()
            return
        
        # Lista de colores profesionales para la gráfica
        paleta_colores = [
            ft.Colors.BLUE_400, ft.Colors.GREEN_400, ft.Colors.ORANGE_400, 
            ft.Colors.PURPLE_400, ft.Colors.RED_400, ft.Colors.CYAN_400
        ]
        
        secciones = []
        
        # i es el índice (0, 1, 2...) para ir saltando de color en la paleta
        for i, (categoria, monto) in enumerate(resumen_gastos.items()):
            # CORRECCIÓN: Eliminamos el argumento 'tooltip'
            secciones.append(
                ft.PieChartSection(
                    value=monto,
                    title=f"{categoria}\n{monto}€", # Ponemos el nombre en el título
                    title_style=ft.TextStyle(size=10, weight="bold", color="white"),
                    color=paleta_colores[i % len(paleta_colores)],
                    radius=40
                )
            )
        
        # Actualizamos la gráfica
        self.grafica.sections = secciones
        
        # Actualizamos el texto de resumen según si hay datos o no
        if not secciones:
            self.txt_resumen.value = "Aún no hay gastos registrados."
            self.txt_resumen.color = ft.Colors.GREY_500
        else:
            self.txt_resumen.value = f"Gastos repartidos en {len(secciones)} categorías"
            self.txt_resumen.color = ft.Colors.BLACK

      # 1. Traemos el presupuesto que el usuario guardó
        presupuesto = CloudManager.obtener_presupuesto(self.user_id)
    
     # 2. Sumamos lo que hay en la gráfica
        gasto_total = sum(s.value for s in secciones)
        restante = presupuesto - gasto_total
    
     # 3. Actualizamos la etiqueta de resumen con color dinámico
        self.txt_resumen.value = f"Presupuesto: {presupuesto}€ | Gastado: {gasto_total:.2f}€\nRestante: {restante:.2f}€"
        self.txt_resumen.color = ft.Colors.GREEN if restante >= 0 else ft.Colors.RED
    
    
            
        self.update()
    #Con did_mount() llamamos a cargar_datos() para que se ejecute en cuanto 
    # la pestaña sea visible, así la gráfica se muestra con datos reales 
    # desde el inicio.
    def did_mount(self):
        
        self.cargar_datos()
