import flet as ft
from supabase import create_client, Client

# --- TUS CREDENCIALES ---
SUPABASE_URL = "https://tgibzetuyldndxwagwwv.supabase.co"
SUPABASE_KEY = "sb_publishable_375xlx2UfsSgqP0o0pWMFQ_K61BNkaQ"

# Inicializamos el túnel hacia la nube
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class CloudManager:
    @staticmethod
    def registrar_usuario(email, password):
        """Crea un usuario y devuelve un mensaje de éxito o error"""
        try:
            auth_response = supabase.auth.sign_up({
                "email": email,
                "password": password,
            })
            return "✅ Registro exitoso. ¡Confirma tu email!"
        except Exception as e:
            # Simplificamos el error para que el usuario lo entienda
            return f"❌ Error: {str(e)}"

    @staticmethod
    def login_usuario(email, password):
        """Valida credenciales y devuelve el ID del usuario si es correcto"""
        try:
            auth_response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password,
            })
            return auth_response.user.id
        except Exception:
            return None
### Fase 7.2: Conectando la Lista de Compras a la Nube
    @staticmethod
    def agregar_producto_db(user_id, nombre_producto, precio_producto, categoría_producto):
        """Inserta un producto en la tabla SQL vinculado al usuario"""
        try:
            res = supabase.table("productos").insert({
                "user_id": user_id, 
                "nombre": nombre_producto,
                "precio":precio_producto,
                "categoria": categoría_producto
            }).execute()
            return res.data[0] # Devolvemos el producto con su ID de la base de datos
        except Exception as e:
            print(f"Error al guardar en nube: {e}")
            return None

    @staticmethod
    def obtener_productos_db(user_id):
        """Trae los productos de este usuario desde la nube"""
        try:
            res = supabase.table("productos").select("*").eq("user_id", user_id).execute()
            return res.data
        except Exception as e:
            print(f"Error al bajar datos: {e}")
            return []

    @staticmethod
    def borrar_producto_db(producto_id):
        """Elimina por ID único de tabla"""
        try:
            supabase.table("productos").delete().eq("id", producto_id).execute()
        except Exception as e:
            print(f"Error al borrar en nube: {e}")


    @staticmethod
    def actualizar_estado_db(producto_id, esta_completado):
        supabase.table("productos").update({"completado": esta_completado}).eq("id", producto_id).execute()
    
   
    # cresar metodo obtener_presupuesto(user_id): debe hacer un select() a la tabla presupuesto.
    #Si no existe presupuesto para ese usuario, debe devolver 0.0

    @staticmethod
    def obtener_presupuesto(user_id):
        """Trae el presupuesto del ususario desde la nube""" 
        try:
            res = supabase.table("presupuestos").select("monto_maximo").eq("user_id",user_id).execute()
            if res.data:
                return res.data[0]['monto_maximo']
            else:
                return 0.0
        except Exception as e:
            print(f"Error al obtener presupuesto: {e}")
            return 0.0
    
    #crear metodo actualizar_presupuesto(user_id, nuevo_monto): 
    # debe hacer un upsert() a la tabla presupuesto con el nuevo monto.
    """upsert() es una combinación de insert() y update(). 
    Si el registro no existe, lo inserta. 
    Si ya existe, lo actualiza con el nuevo monto."""

    @staticmethod
    def actualizar_presupuesto(user_id,nuevo_monto):
        """Actualiza el presupuesto del ususario en la nube"""
        try:
            supabase.table("presupuestos").upsert({"user_id":user_id,
                                                    "monto_maximo": nuevo_monto}).execute()
            return True
        except Exception as e:
            print(f"Error al actualizar presupuesto: {e}")
            return False
    @staticmethod
    def obtener_resumen_gastos(user_id):
        """Trae los productos comprados y los suma por categoría para la gráfica"""
        try:
            # 1. Pedimos a la nube solo los productos que ya marcamos como comprados (completado=True)
            res = supabase.table("productos").select("categoria, precio").eq("user_id", user_id).eq("completado", True).execute()
            
            datos = res.data
            resumen = {}

            # 2. Lógica de Agregación: Sumamos los precios por cada categoría
            for p in datos:
                cat = p['categoria'] if p['categoria'] else "Otros"
                precio = p['precio'] if p['precio'] is not None else 0.0
                
                # Si la categoría ya existe en nuestro resumen, sumamos. Si no, la creamos.
                resumen[cat] = resumen.get(cat, 0) + precio
            
            return resumen 
        except Exception as e:
            print(f"Error al obtener resumen de gastos: {e}")
            return {}
   
