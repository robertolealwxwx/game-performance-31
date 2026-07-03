from typing import List, Dict, Any

class Game:
    def __init__(self, name: str, players: List[str]) -> None:
        """Initialize the Game object with name and players."""
        self.name = name
        self.players = players
        self.scoreboard: Dict[str, int] = {player: 0 for player in players}

    def update_score(self, player: str, points: int) -> None:
        """Update the score for a given player."""
        if player in self.scoreboard:
            self.scoreboard[player] += points
        else:
            raise ValueError(f"Player {player} not found in the game.")

    def get_scores(self) -> Dict[str, int]:
        """Return the current scoreboard."""
        return self.scoreboard

    def game_over(self) -> str:
        """Return the name of the player with the highest score."""
        winner = max(self.scoreboard, key=self.scoreboard.get)
        return f"The winner is {winner} with {self.scoreboard[winner]} points!"

# Example usage:
if __name__ == '__main__':
    game = Game("Super Fun Game", ["Alice", "Bob", "Charlie"])
    game.update_score("Alice", 10)
    game.update_score("Bob", 5)
    game.update_score("Charlie", 8)
    print(game.get_scores())
    print(game.game_over())
