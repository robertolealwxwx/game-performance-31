import json

class GameDataHandler:
    def __init__(self, data_file):
        self.data_file = data_file

    def load_data(self):
        """Load game data from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.data_file} not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON.")
            return {}

    def save_data(self, data):
        """Save game data to a JSON file.""" 
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def update_game_data(self, new_data):
        """Update the existing game data with new data."""
        current_data = self.load_data()
        current_data.update(new_data)
        self.save_data(current_data)

    def get_player_scores(self, player_name):
        """Retrieve scores for a specific player."""
        data = self.load_data()
        return data.get(player_name, {}).get('scores', [])

if __name__ == '__main__':
    handler = GameDataHandler('game_data.json')
    print(handler.load_data())
    handler.update_game_data({'player1': {'scores': [100, 200, 300]}})
    print(handler.get_player_scores('player1'))