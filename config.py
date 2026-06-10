import json
import os

DEFAULT_CONFIG = {
    'window_width': 800,
    'window_height': 600,
    'fullscreen': False,
    'volume': 0.5,
    'graphics_quality': 'high'
}

def load_config(filename='config.json'):
    '''Load configuration from a JSON file with defaults.'''
    if not os.path.isfile(filename):
        return DEFAULT_CONFIG
    with open(filename, 'r') as config_file:
        try:
            user_config = json.load(config_file)
        except json.JSONDecodeError:
            print('Error decoding JSON, using defaults.')
            return DEFAULT_CONFIG
    # Merge user config with defaults
    config = {**DEFAULT_CONFIG, **user_config}
    return config
