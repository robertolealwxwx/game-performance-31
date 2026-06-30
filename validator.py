import re

def validate_username(username):
    """
    Validate the username for game
    - Must be alphanumeric
    - Length between 3 to 15 characters
    """
    if not re.match("^[A-Za-z0-9]{3,15}$", username):
        raise ValueError("Invalid username. Must be 3-15 alphanumeric characters.")


def validate_score(score):
    """
    Validate the game score
    - Must be an integer
    - Must be between 0 and 100
    """
    if not isinstance(score, int):
        raise ValueError("Score must be an integer.")
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100.")


def validate_input(username, score):
    """
    Validate both username and score.
    Raise ValueError for invalid inputs.
    """
    validate_username(username)
    validate_score(score)