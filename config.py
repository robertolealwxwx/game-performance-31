import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Default config file not found: {self.default_config_path}")
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_user_config(self, user_config_path):
        if os.path.exists(user_config_path):
            with open(user_config_path, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json')
    config_loader.load_user_config('user_config.json')
    print(config_loader.get('game_speed', 1.0))