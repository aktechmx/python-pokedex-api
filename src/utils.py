"""Utility functions for images used by the application."""

from io import BytesIO
from pathlib import Path

import requests
from PIL import Image, ImageTk


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ICONS_DIR = PROJECT_ROOT / "assets" / "icons"


def load_pokemon_image(url, size=(260, 260)):
    """Download and prepare a Pokemon image for Tkinter."""

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))
    image = image.convert("RGBA")

    image.thumbnail(
        size,
        Image.Resampling.LANCZOS
    )

    return ImageTk.PhotoImage(image)


def load_ui_icon(filename, size=(28, 28)):
    """Load and resize a local UI icon."""

    icon_path = ICONS_DIR / filename

    if not icon_path.exists():
        raise FileNotFoundError(
            f"UI icon not found: {icon_path}"
        )

    image = Image.open(icon_path)
    image = image.convert("RGBA")

    # Preserve the original aspect ratio
    image.thumbnail(
        size,
        Image.Resampling.LANCZOS
    )

    # Create a transparent canvas with the same size for all icons
    canvas = Image.new(
        "RGBA",
        size,
        (0, 0, 0, 0)
    )

    x = (size[0] - image.width) // 2
    y = (size[1] - image.height) // 2

    canvas.alpha_composite(
        image,
        (x, y)
    )

    return ImageTk.PhotoImage(canvas)