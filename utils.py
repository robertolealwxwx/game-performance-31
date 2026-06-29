import random
import math


def random_choice(choices):
    """Return a random choice from a list."""
    if not choices:
        raise ValueError('The choices list must not be empty.')
    return random.choice(choices)


def distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum."""
    return max(min(value, max_value), min_value)


def load_json(file_path):
    """Load a JSON file and return its content."""
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    """Save data to a JSON file."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
