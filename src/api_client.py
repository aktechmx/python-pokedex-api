"""Poke api client module."""
import requests

BASE_URL = "https://pokeapi.co/api/v2/"

class PokemonNotFoundError(Exception):
    """Raised when the requested Pokemon is not found in the API or does not exist."""

class PokemonAPIError(Exception):
    """Raised when PokéAPI cannot be reached"""


def get_pokemon(pokemon):
    """Get a Pokemon by name or ID."""
    pokemon = str(pokemon).strip().lower()

    url = f"{BASE_URL}pokemon/{pokemon}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 404:
            raise PokemonNotFoundError(
                f"Pokemon '{pokemon}' was not found"
            )
        response.raise_for_status()
    except requests.Timeout as exc:
        raise PokemonAPIError(
            "The request to PokéAPI timed out."
        ) from exc

    response.raise_for_status()

    return response.json()
