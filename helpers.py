import random


def generate_random_position(max_x, max_y):
    """Generate a random (x, y) position within specified boundaries."""
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)


def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def clamp(value, min_value, max_value):
    """Restrict a value to lie within a given range."""
    return max(min_value, min(value, max_value))


def lerp(start, end, t):
    """Linearly interpolate between two values based on t."""
    return (1 - t) * start + t * end


def normalize_vector(vector):
    """Return the normalized version of a vector, or None if the vector is zero."""
    length = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    if length == 0:
        return None
    return (vector[0] / length, vector[1] / length)