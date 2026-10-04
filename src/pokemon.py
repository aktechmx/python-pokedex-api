"""Receives a pokemon name and returns the corresponding pokemon data from the PokeAPI."""


def parse_pokemon_data(data):
    """Parse the pokemon data and return a dictionary with the relevant information."""
    pokemon ={
        "id": data["id"],
        "name": data["name"].capitalize(),
        "height": data["height"] /10,  # Convert decimeters to meters
        "weight": data["weight"] /10,  # Convert hectograms to kilograms
        "types": [type_info["type"]["name"] for type_info in data["types"]],
        "abilities": [ability_info["ability"]["name"] 
                      for ability_info in data["abilities"]],
        "stats": {stat_info["stat"]["name"]: stat_info["base_stat"] 
                  for stat_info in data["stats"]},
        "photo": data["sprites"]["other"]["official-artwork"]["front_default"]     
    }
    return pokemon
