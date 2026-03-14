
```
# 🛒 Mi Lista de la Compra - Multiplataforma

```
<p align="center">
  <img src="assets/screenshot.png" alt="Captura de pantalla" width="300">
</p>
```

Una aplicación moderna, ligera y funcional para gestionar tus compras diarias. Desarrollada íntegramente en **Python** con el framework **Flet**, esta app es capaz de ejecutarse de forma nativa en **Android** y como una **PWA (Progressive Web App)** en cualquier navegador.

##  Características Principales

- **Gestión Intuitiva:** Añade productos rápidamente y márcalos como completados con un efecto visual de tachado.
- **Persistencia Local:** Gracias al uso de `page.client_storage`, tus productos se guardan automáticamente en el dispositivo. ¡No perderás tu lista al cerrar la app!
- **Diseño Responsive:** Interfaz limpia basada en Material Design que se adapta perfectamente a pantallas de móviles y escritorio.
- **Acciones Rápidas:** Botón flotante para añadir ítems y opción de limpieza total de la lista.

##  Desafíos Técnicos Superados

Este proyecto marca mi avance en el desarrollo de software, implementando conceptos avanzados:
- **Programación Orientada a Objetos (POO):** Creación de componentes personalizados mediante clases para manejar cada ítem de la lista de forma independiente.
- **Manejo de Ciclo de Vida y Datos:** Implementación de lógica de guardado y carga de datos para asegurar la persistencia.
- **Arquitectura Multiplataforma:** Configuración de un entorno de desarrollo profesional con Flutter SDK para la generación de binarios APK.

##  Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repo.git
   cd nombre-del-repo
   ```

2. **Configurar el entorno (Python 3.12):**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # En Windows: .\.venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install flet==0.25.0
   ```

4. **Lanzar la aplicación:**
   ```bash
   flet run main.py
   ```

## 📱 Despliegue

- **Android:** Generación de archivo `.apk` mediante `flet build apk`.
- **Web:** Disponible como PWA mediante `flet build web`.

---
Desarrollado por **Daniel** -  
```

---