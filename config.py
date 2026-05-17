from typing import Dict, Any

def load_config(file_path: str) -> Dict[str, Any]:
    """
    Loads configuration settings from a JSON file.

    :param file_path: The path to the JSON configuration file.
    :return: A dictionary containing the configuration settings.
    """
    import json
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config


def save_config(file_path: str, config: Dict[str, Any]) -> None:
    """
    Saves configuration settings to a JSON file.

    :param file_path: The path to the JSON configuration file.
    :param config: A dictionary containing configuration settings to save.
    """
    import json
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)


def get_default_config() -> Dict[str, Any]:
    """
    Returns the default configuration settings.

    :return: A dictionary containing default configuration settings.
    """
    return {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 75,
        'controls': {
            'move_up': 'W',
            'move_down': 'S',
            'move_left': 'A',
            'move_right': 'D'
        }
    }
