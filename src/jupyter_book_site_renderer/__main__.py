from .app import JupyterBookSiteRendererApp


def main(argv=None):
    app = JupyterBookSiteRendererApp()
    app.initialize(argv)
    app.start()

if __name__ == "__main__":
    main()
