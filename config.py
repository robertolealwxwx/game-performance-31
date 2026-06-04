import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 0.5,
    'controls': {
        'move_up': 'W',
        'move_down': 'S',
        'move_left': 'A',
        'move_right': 'D',
        'shoot': 'SPACE'
    }
}

def load_config(file_path='config.json'):
    # Check if the specified config file exists
    if not os.path.isfile(file_path):
        return DEFAULT_CONFIG  # Return defaults if file does not exist
    
    # Load the configuration from the JSON file
    with open(file_path, 'r') as file:
        config = json.load(file)
    
    # Update the default configuration with any loaded settings
    return {**DEFAULT_CONFIG, **config}

if __name__ == '__main__':
    config = load_config()
    print(config)