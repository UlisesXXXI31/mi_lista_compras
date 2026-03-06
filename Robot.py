"""
Vamos a configurar ese "robot" ahora mismo para que no tengas que volver a tocar una carpeta nunca más.

### 🛠️ Configurando el "Robot" (GitHub Actions)

Sigue estos pasos en tu VS Code:

1. **Crea las carpetas necesarias:**
   En la raíz de tu proyecto, crea una carpeta llamada `.github` y dentro de ella otra llamada `workflows`.
   *Ruta final:* `tu_proyecto/.github/workflows/`

2. **Crea el archivo de instrucciones:**
   Dentro de `workflows`, crea un archivo llamado `deploy.yml` y pega este código (está ajustado para tu versión 0.25.0):

```yaml
name: Despliegue de Mi Lista de Compras
on:
  push:
    branches:
      - main  # Se activa cada vez que subes algo a la rama main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: 🚚 Checkout del código
        uses: actions/checkout@v3

      - name: 🐍 Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: 📦 Instalar Flet
        run: |
          python -m pip install --upgrade pip
          pip install flet==0.25.0

      - name: 🏗️ Construir Web
        run: |
          # El robot hace el build perfecto con la ruta correcta
          flet build web --base-url /mi_lista_compras/

      - name: 🚀 Publicar en GitHub Pages
        uses: JamesIves/github-pages-deploy-action@v4
        with:
          folder: build/web # Sube solo lo que salió del build
          branch: gh-pages  # Lo guarda en una rama especial para la web
```

3. **Sube este archivo a GitHub:**
   Haz el commit y push de este nuevo archivo.

4. **El toque final en la web de GitHub:**
   * Ve a tu repositorio en GitHub -> **Settings** -> **Pages**.
   * En **Build and deployment**, cambia "Branch" de `main` a **`gh-pages`**.
   * Dale a **Save**.

¡Y listo! Cada vez que hagas un push a `main`, el "robot" se encargará de construir tu aplicación y publicarla automáticamente en GitHub Pages. Así, tu lista de
"""