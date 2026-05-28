import json
from utils import calculate_score
from constants import MAX_SCORE

class GameHandler:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0

    def update_score(self, points):
        """Update the player's score and limit it to MAX_SCORE."""
        self.score += points
        if self.score > MAX_SCORE:
            self.score = MAX_SCORE

    def get_score(self):
        """Return the current score of the player."""
        return self.score

    def save_score(self, filename='scores.json'):
        """Save the current score to a JSON file."""
        data = {'player_name': self.player_name, 'score': self.score}
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_score(self, filename='scores.json'):
        """Load player score from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.player_name = data['player_name']
                self.score = data['score']
        except (FileNotFoundError, KeyError):
            print('Score file not found or corrupted')
            self.score = 0

if __name__ == '__main__':
    handler = GameHandler('Player1')
    handler.update_score(50)
    print(f'Score: {handler.get_score()}')
    handler.save_score()