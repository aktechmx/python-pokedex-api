"""Main entry point for the Pokemon API client application."""
from ui.app import PokedexApp


def main():

    app = PokedexApp()

    app.mainloop()


if __name__ == "__main__":
    main()
