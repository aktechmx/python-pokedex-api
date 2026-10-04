"""Search Frame module for the Pokedex application."""

import tkinter as tk
from tkinter import messagebox

from src.api_client import (
    get_pokemon,
    PokemonNotFoundError,
    PokemonAPIError,
)
from src.pokemon import parse_pokemon_data
from ui.styles import COLORS
from ui.window_controls import WindowControls, bind_drag
from ui.rounded_widgets import RoundedFrame, RoundedButton


class SearchFrame(tk.Frame):
    """Frame used to search for Pokemon."""

    def __init__(self, parent, on_pokemon_found):
        super().__init__(
            parent,
            bg=COLORS["transparent"]
        )

        self.on_pokemon_found = on_pokemon_found

        self.create_widgets()

        self.search_entry.focus()

        self.search_entry.bind(
            "<Return>",
            lambda _event: self.search_pokemon()
        )

    def create_widgets(self):
        """Create widgets for the Pokemon search screen."""

        # -------------------------------------------------
        # Main rounded Pokedex body
        # -------------------------------------------------

        pokedex = RoundedFrame(
            self,
            bg_color=COLORS["pokedex_red"],
            radius=24,
            padding=25
        )

        pokedex.pack(
            expand=True,
            fill="both",
            padx=40,
            pady=30
        )

        pokedex_body = pokedex.content

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        header = tk.Frame(
            pokedex_body,
            bg=COLORS["pokedex_red"]
        )

        header.pack(
            fill="x",
            pady=(0, 15)
        )

        # Custom PNG window controls
        window_controls = WindowControls(
            header,
            self.master
        )

        window_controls.pack(
            side="left"
        )

        # Empty draggable area
        drag_area = tk.Frame(
            header,
            bg=COLORS["pokedex_red"],
            height=28
        )

        drag_area.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(12, 12)
        )

        # Pokedex title
        title_label = tk.Label(
            header,
            text="POKÉDEX",
            font=("Arial", 24, "bold"),
            fg=COLORS["text_light"],
            bg=COLORS["pokedex_red"]
        )

        title_label.pack(
            side="right"
        )

        # Allow window movement
        bind_drag(
            header,
            self.master
        )

        bind_drag(
            drag_area,
            self.master
        )

        bind_drag(
            title_label,
            self.master
        )

        # -------------------------------------------------
        # Rounded inner screen
        # -------------------------------------------------

        screen = RoundedFrame(
            pokedex_body,
            bg_color=COLORS["screen"],
            radius=14,
            padding=35
        )

        screen.pack(
            fill="both",
            expand=True
        )

        screen_body = screen.content

        # -------------------------------------------------
        # Search content
        # -------------------------------------------------

        search_container = tk.Frame(
            screen_body,
            bg=COLORS["screen"]
        )

        search_container.pack(
            expand=True,
            fill="both"
        )

        tk.Label(
            search_container,
            text="Who's that Pokémon?",
            font=("Arial", 28, "bold"),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack(
            pady=(40, 10)
        )

        tk.Label(
            search_container,
            text="Enter a Pokémon name or Pokédex ID",
            font=("Arial", 12),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack(
            pady=(0, 25)
        )

        # -------------------------------------------------
        # Search entry
        # -------------------------------------------------

        self.search_entry = tk.Entry(
            search_container,
            font=("Arial", 18),
            justify="center",
            bg=COLORS["input"],
            fg=COLORS["text"],
            relief="solid",
            bd=1
        )

        self.search_entry.pack(
            ipadx=20,
            ipady=10,
            padx=100,
            fill="x"
        )

        # -------------------------------------------------
        # Rounded Search button
        # -------------------------------------------------

        search_button = RoundedButton(
            search_container,
            text="SEARCH",
            command=self.search_pokemon,
            width=145,
            height=44,
            radius=16,
            bg_color=COLORS["pokedex_dark"],
            hover_color=COLORS["pokedex_red"],
            text_color=COLORS["text_light"]
        )

        search_button.pack(
            pady=(30, 0)
        )

    def search_pokemon(self):
        """Search for a Pokemon using its name or Pokedex ID."""

        pokemon_query = self.search_entry.get().strip()

        if not pokemon_query:
            messagebox.showwarning(
                "Missing Pokémon",
                "Please enter a Pokémon name or Pokédex ID."
            )
            return

        try:
            data = get_pokemon(
                pokemon_query
            )

            pokemon = parse_pokemon_data(
                data
            )

        except PokemonNotFoundError:
            messagebox.showerror(
                "Pokémon not found",
                "Please check the Pokémon name or ID and try again."
            )
            return

        except PokemonAPIError:
            messagebox.showerror(
                "Connection error",
                "Unable to connect to PokéAPI."
            )
            return

        self.on_pokemon_found(
            pokemon
        )
