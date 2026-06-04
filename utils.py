import random
import math

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def generate_random_position(bounds):
    """Generate a random position within given bounds."""
    x = random.uniform(bounds['x_min'], bounds['x_max'])
    y = random.uniform(bounds['y_min'], bounds['y_max'])
    return (x, y)


def clamp(value, min_value, max_value):
    """Clamp a value between min and max."""
    return max(min_value, min(value, max_value))


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