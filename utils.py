import json

class GameDataError(Exception):
    """Custom exception for game data errors."""
    pass


def load_game_data(file_path):
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise GameDataError(f'File not found: {file_path}')
    except json.JSONDecodeError:
        raise GameDataError(f'Invalid JSON in file: {file_path}')
    except Exception as e:
        raise GameDataError(f'An error occurred: {str(e)}')


def save_game_data(file_path, data):
    """Save game data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise GameDataError(f'Failed to save data: {str(e)}')


def validate_game_data(data):
    """Validate game data structure."""
    required_keys = ['name', 'score', 'level']
    if not all(key in data for key in required_keys):
        raise GameDataError('Missing required game data fields.')
    return True