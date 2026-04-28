import asyncio

from . import JupyterBookSiteRenderer

if __name__ == "__main__":
    app = JupyterBookSiteRenderer()
    asyncio.run(app.start())
