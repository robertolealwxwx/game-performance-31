class GameConfig:
    def __init__(self):
        self.settings = {
            'screen_width': 800,
            'screen_height': 600,
            'fps': 60,
            'background_color': (0, 0, 0),
            'title': 'Game Title'
        }

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value

    def load_settings(self, file_path):
        import json
        try:
            with open(file_path, 'r') as f:
                self.settings.update(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Error loading settings: {e}')

    def save_settings(self, file_path):
        import json
        with open(file_path, 'w') as f:
            json.dump(self.settings, f, indent=4)

# Example of usage:
# config = GameConfig()
# config.load_settings('config.json')
# print(config.get_setting('title'))
