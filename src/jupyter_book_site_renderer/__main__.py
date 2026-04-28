import asyncio

from . import MySTSiteRenderer

if __name__ == "__main__":
    app = MySTSiteRenderer()
    asyncio.run(app.start())
