# SPDX-FileCopyrightText: 2026-present Angus Hollands <goosey15@gmail.com>
#
# SPDX-License-Identifier: MIT
import asyncio
import pathlib

from traitlets.config import Application
from traitlets import List, Unicode

from .renderer import JupyterBookSiteRenderer


class JupyterBookSiteRendererApp(Application):
    """
    Build Jupyter Book from pre-built AST.
    If the AST does not exist, attempt a source build.
    """

    name = Unicode("jupyter-book-site-renderer-app")

    site_path = Unicode(None, config=True, allow_none=False)
    html_path = Unicode("html", config=True)
    base_url = Unicode("/", config=True)

    classes = List([JupyterBookSiteRenderer])

    aliases = {
        **Application.aliases,
        "site": "JupyterBookSiteRendererApp.site_path",
        "html": "JupyterBookSiteRendererApp.html_path",
        "base-url": "JupyterBookSiteRendererApp.base_url",
    }

    async def build(self):
        self.load_config_file("jupyter_book_site_renderer")
        self.load_config_environ()

        renderer = JupyterBookSiteRenderer(parent=self)
        await renderer.render_html(
            site_path=pathlib.Path(self.site_path),
            html_path=pathlib.Path(self.html_path),
            base_url=self.base_url,
        )

    def start(self):
        asyncio.run(self.build())
