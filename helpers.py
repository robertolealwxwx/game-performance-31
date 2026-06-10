import random
import math

def clamp(value, min_value, max_value):
    """Restrict a value within a range."""
    return max(min(value, max_value), min_value)


def distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def random_choice(sequence):
    """Return a random element from a non-empty sequence."""
    if not sequence:
        raise ValueError('Cannot choose from an empty sequence')
    return random.choice(sequence)


def linear_interpolation(start, end, ratio):
    """Perform linear interpolation between start and end based on ratio."""
    return start + (end - start) * ratio


def load_from_json(file_path):
    """Load data from a JSON file."""
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def save_to_json(data, file_path):
    """Save data to a JSON file."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
