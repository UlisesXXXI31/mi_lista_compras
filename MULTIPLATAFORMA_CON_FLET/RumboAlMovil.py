#### Fase 6: ¡Rumbo al Móvil! 📱🚀

"""
Ahora que tu app es perfecta y tiene memoria, el siguiente paso es verla en tu teléfono. 

Para Android, Python necesita "empaquetar" todo. El proceso es un poco técnico, pero Flet lo hace muy fácil. Necesitas instalar una herramienta llamada **`flet-cli`** (que ya deberías tener, pero lo comprobaremos).

**Tu siguiente paso de tutoría:**
1. En tu terminal de VS Code, escribe este comando para comprobar si tienes las herramientas listas:
   `.\.venv\Scripts\flet --version`
2. Si te da un número de versión, estamos listos.
"""
### Lo que debes saber sobre el "Rumbo al Móvil"
"""
Si el comando te responde con una versión (probablemente la 0.25.0), significa que la herramienta está ahí. Pero aquí viene la **gran noticia (y el gran reto)**:

Para convertir tu código de Python en una **App de Android (.APK)**, Flet utiliza por debajo 
una herramienta llamada **Flutter** (que es de Google). Por lo tanto, para que tu ordenador 
pueda "fabricar" la aplicación, necesitamos instalar un par de cosas pesadas:

1.  **Flutter SDK:** El motor que construye apps móviles.
2.  **Android Studio:** Para tener las herramientas de empaquetado de Android.

**¿Es difícil?** No, pero lleva tiempo y espacio en disco (unos 10-15 GB). 

"""