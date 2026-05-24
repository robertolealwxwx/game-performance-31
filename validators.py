def validate_score(score):
    """
    Validates the score provided by the player.
    Returns True if the score is an integer between 0 and 100,
    raises ValueError if invalid.
    """
    if not isinstance(score, int):
        raise ValueError('Score must be an integer.')
    if score < 0 or score > 100:
        raise ValueError('Score must be between 0 and 100.')
    return True


def validate_player_name(name):
    """
    Validates the player's name.
    Returns True if the name is a non-empty string,
    raises ValueError if invalid.
    """
    if not isinstance(name, str):
        raise ValueError('Player name must be a string.')
    if len(name.strip()) == 0:
        raise ValueError('Player name cannot be empty.')
    return True


def validate_game_level(level):
    """
    Validates the game level.
    Returns True if the level is in the acceptable range,
    raises ValueError if invalid.
    """
    if not isinstance(level, int):
        raise ValueError('Game level must be an integer.')
    if level < 1 or level > 10:
        raise ValueError('Game level must be between 1 and 10.')
    return True
