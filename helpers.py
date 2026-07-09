import json
from typing import Any, Dict

def load_game_data(file_path: str) -> Dict[str, Any]:
    """
    Load game data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        Dict[str, Any]: The parsed JSON data as a Python dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    """
    Save game data to a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        data (Dict[str, Any]): The data to save in JSON format.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path: str, key: str, value: Any) -> None:
    """
    Update specific key in the game data JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        key (str): The key to update in the data.
        value (Any): The new value to set for the key.
    """
    data = load_game_data(file_path)
    data[key] = value
    save_game_data(file_path, data)
