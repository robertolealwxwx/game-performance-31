class GameError(Exception):
    """Base class for game related errors."""
    pass

class InitializationError(GameError):
    """Raised when initialization fails."""
    def __init__(self, message):
        super().__init__(f'Initialization Error: {message}')

class ResourceNotFoundError(GameError):
    """Raised when a required resource is not found."""
    def __init__(self, resource):
        super().__init__(f'Resource Not Found: {resource}')

class InputError(GameError):
    """Raised when there is invalid input."""
    def __init__(self, input_value):
        super().__init__(f'Invalid Input: {input_value}')

# Example usage in game component

def load_resource(resource_name):
    resources = {'hero': 'hero_model', 'enemy': 'enemy_model'}
    if resource_name not in resources:
        raise ResourceNotFoundError(resource_name)
    return resources[resource_name]


def initialize_game(config):
    if 'level' not in config:
        raise InitializationError('Config must include level')
    return True