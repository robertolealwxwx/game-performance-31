import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filepath):
            raise ConfigError(f"Configuration file not found: {self.filepath}")
        
        try:
            with open(self.filepath, 'r') as config_file:
                return json.load(config_file)
        except json.JSONDecodeError as e:
            raise ConfigError(f"Error parsing JSON in config file: {str(e)}")
        except Exception as e:
            raise ConfigError(f"An unexpected error occurred: {str(e)}")

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def save(self):
        try:
            with open(self.filepath, 'w') as config_file:
                json.dump(self.config_data, config_file, indent=4)
        except Exception as e:
            raise ConfigError(f"Failed to save config file: {str(e)}")

# Example usage:
# config = Config('config.json')
# print(config.get('some_key', 'default_value'))