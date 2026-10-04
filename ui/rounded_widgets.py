"""Reusable rounded widgets for the Pokedex UI."""

import tkinter as tk


class RoundedFrame(tk.Canvas):
    """Canvas-based frame with rounded corners."""

    def __init__(
        self,
        parent,
        bg_color,
        radius=20,
        padding=0,
        **kwargs
    ):
        parent_bg = parent.cget("bg")

        super().__init__(
            parent,
            bg=parent_bg,
            highlightthickness=0,
            bd=0,
            **kwargs
        )

        self.bg_color = bg_color
        self.radius = radius
        self.padding = padding

        self.content = tk.Frame(
            self,
            bg=bg_color
        )

        self.content_window = self.create_window(
            padding,
            padding,
            anchor="nw",
            window=self.content
        )

        self.bind(
            "<Configure>",
            self._resize
        )

    def _resize(self, event):
        """Redraw rounded background when the widget changes size."""

        width = event.width
        height = event.height

        self.delete("rounded_background")

        radius = min(
            self.radius,
            width // 2,
            height // 2
        )

        # Center rectangles
        self.create_rectangle(
            radius,
            0,
            width - radius,
            height,
            fill=self.bg_color,
            outline="",
            tags="rounded_background"
        )

        self.create_rectangle(
            0,
            radius,
            width,
            height - radius,
            fill=self.bg_color,
            outline="",
            tags="rounded_background"
        )

        # Rounded corners
        self.create_oval(
            0,
            0,
            radius * 2,
            radius * 2,
            fill=self.bg_color,
            outline="",
            tags="rounded_background"
        )

        self.create_oval(
            width - radius * 2,
            0,
            width,
            radius * 2,
            fill=self.bg_color,
            outline="",
            tags="rounded_background"
        )

        self.create_oval(
            0,
            height - radius * 2,
            radius * 2,
            height,
            fill=self.bg_color,
            outline="",
            tags="rounded_background"
        )

        self.create_oval(
            width - radius * 2,
            height - radius * 2,
            width,
            height,
            fill=self.bg_color,
            outline="",
            tags="rounded_background"
        )

        self.tag_lower("rounded_background")

        content_width = max(
            width - self.padding * 2,
            1
        )

        content_height = max(
            height - self.padding * 2,
            1
        )

        self.itemconfigure(
            self.content_window,
            width=content_width,
            height=content_height
        )


class RoundedButton(tk.Canvas):
    """Simple rounded button with hover effect."""

    def __init__(
        self,
        parent,
        text,
        command,
        width=120,
        height=38,
        radius=16,
        bg_color="#B94450",
        hover_color="#D95763",
        text_color="#FFFFFF"
    ):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg=parent.cget("bg"),
            highlightthickness=0,
            bd=0,
            cursor="hand2"
        )

        self.command = command
        self.width = width
        self.height = height
        self.radius = radius
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text = text

        self.draw(bg_color)

        self.bind(
            "<Enter>",
            lambda event: self.draw(self.hover_color)
        )

        self.bind(
            "<Leave>",
            lambda event: self.draw(self.bg_color)
        )

        self.bind(
            "<Button-1>",
            lambda event: self.command()
        )

    def draw(self, color):
        """Draw the button."""

        self.delete("all")

        radius = self.radius
        width = self.width
        height = self.height

        self.create_rectangle(
            radius,
            0,
            width - radius,
            height,
            fill=color,
            outline=""
        )

        self.create_rectangle(
            0,
            radius,
            width,
            height - radius,
            fill=color,
            outline=""
        )

        self.create_oval(
            0,
            0,
            radius * 2,
            radius * 2,
            fill=color,
            outline=""
        )

        self.create_oval(
            width - radius * 2,
            0,
            width,
            radius * 2,
            fill=color,
            outline=""
        )

        self.create_oval(
            0,
            height - radius * 2,
            radius * 2,
            height,
            fill=color,
            outline=""
        )

        self.create_oval(
            width - radius * 2,
            height - radius * 2,
            width,
            height,
            fill=color,
            outline=""
        )

        self.create_text(
            width / 2,
            height / 2,
            text=self.text,
            fill=self.text_color,
            font=("Arial", 11, "bold")
        )