"""Main entry point for the Pokemon API client application."""
import tkinter as tk

from ui.search_frame import SearchFrame
from ui.pokemon_frame import PokemonFrame
from ui.styles import (
    COLORS,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)
from src.utils import load_ui_icon

class PokedexApp(tk.Tk):
    """Main application class for the Pokemon API client."""

    def __init__(self):
        super().__init__()

        self.app_icon = load_ui_icon(
            "pokeball.ico",
            size=(32, 32)
        )

        self.iconphoto(
            True,
            self.app_icon
        )
        self.bind("<Map>", self.restore_window_style)
        self.bind("<Escape>", lambda event: self.close_window())

        self.title("Pokédex API Client")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(900, 680)
        self.configure(bg=COLORS["transparent"])

        self.wm_attributes(
            "-transparentcolor",
            COLORS["transparent"]
        )


        self.drag_x = 0
        self.drag_y = 0

        self.is_maximized = False
        self.normal_geometry = None

        # Transparent Window BG
        self.configure(
            bg=COLORS["transparent"]
        )

        self.current_frame = None

        self.show_search_frame()
    def start_move(self, event):
        """Store the mouse position before dragging the window."""

        if self.is_maximized:
            return

        self.drag_x = event.x_root - self.winfo_x()
        self.drag_y = event.y_root - self.winfo_y()


    def move_window(self, event):
        """Move the application window while dragging."""

        if self.is_maximized:
            return

        x = event.x_root - self.drag_x
        y = event.y_root - self.drag_y

        self.geometry(f"+{x}+{y}")


    def close_window(self):
        """Close the application."""

        self.destroy()


    def minimize_window(self):
        """Minimize the application."""

        self.overrideredirect(False)
        self.iconify()


    def restore_window_style(self, _event=None):
        """Restore the frameless style after returning from minimized state."""

        if self.state() == "normal":
            self.overrideredirect(True)


    def toggle_maximize(self):
        """Toggle between maximized and normal window size."""

        if not self.is_maximized:

            self.normal_geometry = self.geometry()

            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            self.geometry(
                f"{screen_width}x{screen_height}+0+0"
            )

            self.is_maximized = True

        else:

            if self.normal_geometry:
                self.geometry(self.normal_geometry)

            self.is_maximized = False
    def change_frame(self, frame):
        """Replace the currently displayed frame."""

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame

        self.current_frame.pack(
            fill="both",
            expand=True
        )

    def show_search_frame(self):
        """Display the Pokemon search screen."""

        frame = SearchFrame(
            self,
            on_pokemon_found = self.show_pokemon_frame
        )

        self.change_frame(frame)

    def show_pokemon_frame(self, pokemon):
        """Display information about the selected Pokemon."""

        frame = PokemonFrame(
            self,
            pokemon=pokemon,
            on_back=self.show_search_frame
        )

        self.change_frame(frame)
