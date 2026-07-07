import json


def load_game_data(file_path):
    """
    Load game data from a JSON file.
    :param file_path: Path to the JSON file
    :return: Parsed JSON data as a dictionary
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading game data: {e}")
        return {}


def save_game_data(file_path, data):
    """
    Save game data to a JSON file.
    :param file_path: Path to the JSON file
    :param data: Data to save (should be serializable)
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Game data saved successfully to {file_path}")
    except (IOError, TypeError) as e:
        print(f"Error saving game data: {e}")


def update_game_score(data, player_id, score_increment):
    """
    Update the player's score in the game data.
    :param data: Game data dictionary
    :param player_id: ID of the player
    :param score_increment: Amount to increment the score by
    """
    if player_id in data:
        data[player_id]['score'] += score_increment
        print(f"Updated score for player {player_id}: {data[player_id]['score']}")
    else:
        print(f"Player ID {player_id} not found in data.")
