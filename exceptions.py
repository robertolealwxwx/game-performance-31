class GameError(Exception):
    """Custom exception for game errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(GameError):
    """Exception raised for invalid input in game settings."""
    pass

class ResourceNotFoundError(GameError):
    """Exception raised when a game resource is not found."""
    pass

class NetworkError(GameError):
    """Exception raised for network-related issues."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

if __name__ == '__main__':
    try:
        raise InvalidInputError('Input value is not valid')
    except InvalidInputError as e:
        print(e.message)