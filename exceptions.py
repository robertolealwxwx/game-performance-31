class GameError(Exception):
    """Base class for all game-related exceptions."""
    pass

class InvalidInputError(GameError):
    """Raised when the input is invalid."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class PlayerNotFoundError(GameError):
    """Raised when a player is not found."""
    def __init__(self, player_id: str) -> None:
        super().__init__(f'Player with ID {player_id} not found.')

class LevelNotLoadedError(GameError):
    """Raised when a game level fails to load."""
    def __init__(self, level_name: str) -> None:
        super().__init__(f'Level {level_name} could not be loaded.')

class InsufficientResourcesError(GameError):
    """Raised when there are not enough resources."""
    def __init__(self, resource: str, available: int, required: int) -> None:
        message = f'Insufficient resources: {resource} (Available: {available}, Required: {required})'
        super().__init__(message)