class GameError(Exception):
    """Base class for all game-related exceptions."""
    pass

class PlayerError(GameError):
    """Exception raised for player-related errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class GameResourceError(GameError):
    """Exception raised for issues with game resources."""
    def __init__(self, resource, message):
        self.resource = resource
        self.message = message
        super().__init__(self.message)

def load_player_data(player_id):
    """Loads player data by player_id. Raises PlayerError if not found."""
    try:
        if player_id <= 0:
            raise PlayerError('Invalid player ID provided.')
        data = get_player_data_from_db(player_id)  # Hypothetical function
        if not data:
            raise PlayerError(f'Player with ID {player_id} not found.')
        return data
    except PlayerError as e:
        print(e)
        return None

def load_game_resources(resource_name):
    """Loads game resources. Raises GameResourceError if not available."""
    try:
        if not resource_name:
            raise GameResourceError(resource_name, 'Resource name cannot be empty.')
        resource = get_resource(resource_name)  # Hypothetical function
        if resource is None:
            raise GameResourceError(resource_name, 'Resource not found.')
        return resource
    except GameResourceError as e:
        print(e)
        return None
