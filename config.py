import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.default_config.copy()

    def load_config(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                try:
                    user_config = json.load(file)
                    self.config.update(user_config)
                except json.JSONDecodeError:
                    print('Error: Invalid JSON format in configuration file.')
        else:
            print(f'Warning: Configuration file {filepath} not found, using defaults.')

    def get(self, key, default=None):
        return self.config.get(key, default)

# Default configuration
default_config = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 0.8,
    'controls': {
        'jump': 'space',
        'shoot': 'ctrl'
    }
}

# Usage example
config_loader = ConfigLoader(default_config)
config_loader.load_config('user_config.json')

# Accessing a configuration value
volume = config_loader.get('volume')
print(f'Volume level: {volume}')
