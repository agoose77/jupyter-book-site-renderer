import asyncio

from .app import JupyterBookSiteRendererApp

if __name__ == "__main__":
    app = JupyterBookSiteRendererApp()
    asyncio.run(app.start())
