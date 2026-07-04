import json
import os


def load_game_data(filepath):
    """
    Load game data from a JSON file.
    Args:
        filepath (str): Path to the JSON file.
    Returns:
        dict: Parsed JSON data.
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, 'r') as file:
        return json.load(file)


def save_game_data(filepath, data):
    """
    Save game data to a JSON file.
    Args:
        filepath (str): Path to the JSON file.
        data (dict): Game data to save.
    Raises:
        IOError: If the file cannot be written.
    """
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to file: {filepath}. {e}")


def update_game_data(filepath, updates):
    """
    Update existing game data with new information.
    Args:
        filepath (str): Path to the JSON file.
        updates (dict): Updates to merge into existing data.
    """
    current_data = load_game_data(filepath)
    current_data.update(updates)
    save_game_data(filepath, current_data)
