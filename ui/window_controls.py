"""Custom window controls for the Pokedex application."""

import tkinter as tk

from src.utils import load_ui_icon
from ui.styles import COLORS


class WindowControls(tk.Frame):
    """Frameless window controls using custom PNG icons."""

    def __init__(self, parent, app):
        super().__init__(
            parent,
            bg=COLORS["pokedex_red"]
        )

        self.app = app

        # Keep references to avoid Tkinter garbage collection
        self.close_icon = load_ui_icon(
            "cerrar.png",
            size=(28, 28)
        )

        self.minimize_icon = load_ui_icon(
            "minimizar.png",
            size=(28, 28)
        )

        self.restore_icon = load_ui_icon(
            "restaurar.png",
            size=(28, 28)
        )

        self.create_widgets()

    def create_widgets(self):
        """Create the three window control buttons."""

        self.create_button(
            self.close_icon,
            self.app.close_window
        ).pack(
            side="left",
            padx=(0, 3)
        )

        self.create_button(
            self.minimize_icon,
            self.app.minimize_window
        ).pack(
            side="left",
            padx=3
        )

        self.create_button(
            self.restore_icon,
            self.app.toggle_maximize
        ).pack(
            side="left",
            padx=(3, 0)
        )

    def create_button(self, image, command):
        """Create a flat image-based window button."""

        return tk.Button(
            self,
            image=image,
            command=command,
            bg=COLORS["pokedex_red"],
            activebackground=COLORS["pokedex_red"],
            relief="flat",
            overrelief="flat",
            borderwidth=0,
            highlightthickness=0,
            padx=0,
            pady=0,
            cursor="hand2",
            takefocus=False
        )


def bind_drag(widget, app):
    """Make a widget usable as a window drag area."""

    widget.bind(
        "<ButtonPress-1>",
        app.start_move
    )

    widget.bind(
        "<B1-Motion>",
        app.move_window
    )