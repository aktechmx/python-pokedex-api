"""Pokemon Frame module for the Pokedex application."""

import tkinter as tk

from src.utils import load_pokemon_image
from ui.styles import COLORS
from ui.window_controls import WindowControls, bind_drag
from ui.rounded_widgets import RoundedFrame, RoundedButton


class PokemonFrame(tk.Frame):
    """Frame used to display Pokemon information."""

    def __init__(self, parent, pokemon, on_back):
        super().__init__(
            parent,
            bg=COLORS["transparent"]
        )

        self.pokemon = pokemon
        self.on_back = on_back
        self.pokemon_photo = None

        self.create_widgets()

    def create_widgets(self):
        """Create widgets used to display Pokemon information."""

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

        # Window controls
        window_controls = WindowControls(
            header,
            self.master
        )

        window_controls.pack(
            side="left"
        )

        # Draggable empty area
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

        # Window dragging
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
            padding=25
        )

        screen.pack(
            fill="both",
            expand=True
        )

        screen_body = screen.content

        screen_body.columnconfigure(
            0,
            weight=1
        )

        screen_body.columnconfigure(
            1,
            weight=1
        )

        screen_body.rowconfigure(
            0,
            weight=0
        )

        screen_body.rowconfigure(
            1,
            weight=1
        )

        screen_body.rowconfigure(
            2,
            weight=0
        )

        # -------------------------------------------------
        # Pokemon title
        # -------------------------------------------------

        title_frame = tk.Frame(
            screen_body,
            bg=COLORS["screen"]
        )

        title_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 15)
        )

        tk.Label(
            title_frame,
            text=f"#{self.pokemon['id']:04d}",
            font=("Arial", 13),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack()

        tk.Label(
            title_frame,
            text=self.pokemon["name"],
            font=("Arial", 28, "bold"),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack()

        # -------------------------------------------------
        # Responsive content area
        # -------------------------------------------------

        content_frame = tk.Frame(
            screen_body,
            bg=COLORS["screen"]
        )

        content_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        # 40% image / 60% information
        content_frame.columnconfigure(
            0,
            weight=4
        )

        content_frame.columnconfigure(
            1,
            weight=6
        )

        content_frame.rowconfigure(
            0,
            weight=1
        )

        # -------------------------------------------------
        # Left panel - Pokemon image
        # -------------------------------------------------

        left_panel = tk.Frame(
            content_frame,
            bg=COLORS["screen"]
        )

        left_panel.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(10, 25)
        )

        self.pokemon_photo = load_pokemon_image(
            self.pokemon["photo"],
            size=(230, 230)
        )

        image_label = tk.Label(
            left_panel,
            image=self.pokemon_photo,
            bg=COLORS["screen"]
        )

        image_label.pack(
            expand=True
        )

        # -------------------------------------------------
        # Right panel - Pokemon information
        # -------------------------------------------------

        right_panel = tk.Frame(
            content_frame,
            bg=COLORS["screen"]
        )

        right_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(25, 10)
        )

        pokemon_types = " / ".join(
            pokemon_type.replace("-", " ").title()
            for pokemon_type in self.pokemon["types"]
        )

        tk.Label(
            right_panel,
            text=f"Type: {pokemon_types}",
            font=("Arial", 13, "bold"),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack(
            anchor="w",
            pady=(0, 7)
        )

        tk.Label(
            right_panel,
            text=f"Height: {self.pokemon['height']} m",
            font=("Arial", 12),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack(
            anchor="w",
            pady=2
        )

        tk.Label(
            right_panel,
            text=f"Weight: {self.pokemon['weight']} kg",
            font=("Arial", 12),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack(
            anchor="w",
            pady=2
        )

        abilities = ", ".join(
            ability.replace("-", " ").title()
            for ability in self.pokemon["abilities"]
        )

        tk.Label(
            right_panel,
            text=f"Abilities: {abilities}",
            font=("Arial", 12),
            fg=COLORS["text"],
            bg=COLORS["screen"],
            wraplength=420,
            justify="left"
        ).pack(
            anchor="w",
            pady=(2, 10)
        )

        # -------------------------------------------------
        # Base Stats
        # -------------------------------------------------

        tk.Label(
            right_panel,
            text="Base Stats",
            font=("Arial", 13, "bold"),
            fg=COLORS["text"],
            bg=COLORS["screen"]
        ).pack(
            anchor="w",
            pady=(5, 5)
        )

        stat_names = {
            "hp": "HP",
            "attack": "Attack",
            "defense": "Defense",
            "special-attack": "Sp. Attack",
            "special-defense": "Sp. Defense",
            "speed": "Speed",
        }

        for stat, value in self.pokemon["stats"].items():

            stat_frame = tk.Frame(
                right_panel,
                bg=COLORS["screen"]
            )

            stat_frame.pack(
                fill="x",
                pady=3
            )

            stat_frame.columnconfigure(
                0,
                minsize=90
            )

            stat_frame.columnconfigure(
                1,
                minsize=40
            )

            stat_frame.columnconfigure(
                2,
                weight=1
            )

            # Stat name
            tk.Label(
                stat_frame,
                text=stat_names.get(stat, stat),
                anchor="w",
                font=("Arial", 10, "bold"),
                fg=COLORS["text"],
                bg=COLORS["screen"]
            ).grid(
                row=0,
                column=0,
                sticky="w"
            )

            # Stat value
            tk.Label(
                stat_frame,
                text=str(value),
                font=("Arial", 10),
                fg=COLORS["text"],
                bg=COLORS["screen"]
            ).grid(
                row=0,
                column=1,
                padx=(5, 10)
            )

            # Responsive stat bar
            bar_background = tk.Frame(
                stat_frame,
                bg=COLORS["screen_border"],
                height=12
            )

            bar_background.grid(
                row=0,
                column=2,
                sticky="ew"
            )

            bar_background.grid_propagate(False)

            percentage = min(
                value / 255,
                1
            )

            bar = tk.Frame(
                bar_background,
                bg=COLORS["pokedex_dark"]
            )

            bar.place(
                x=0,
                y=0,
                relheight=1,
                relwidth=percentage
            )

        # -------------------------------------------------
        # Rounded Back button
        # -------------------------------------------------

        back_button = RoundedButton(
            screen_body,
            text="←  BACK",
            command=self.on_back,
            width=125,
            height=40,
            radius=16,
            bg_color=COLORS["pokedex_dark"],
            hover_color=COLORS["pokedex_red"],
            text_color=COLORS["text_light"]
        )

        back_button.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=(15, 0)
        )
