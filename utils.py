import json

def load_game_data(file_path):
    """
    Loads game data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing game data.
    
    Returns:
        dict: Parsed game data as a dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(data, file_path):
    """
    Saves game data to a JSON file.
    
    Args:
        data (dict): Game data to save.
        file_path (str): Path to the JSON file where data will be saved.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path, updates):
    """
    Updates the game data with new values.
    
    Args:
        file_path (str): Path to the JSON file containing game data.
        updates (dict): Dictionary containing updates to apply.
    """
    data = load_game_data(file_path)
    data.update(updates)
    save_game_data(data, file_path)