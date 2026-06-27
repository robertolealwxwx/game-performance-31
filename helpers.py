import random
import math

def clamp(value, min_value, max_value):
    """Clamp the value between min_value and max_value."""
    return max(min(value, max_value), min_value)


def lerp(start, end, t):
    """Linear interpolation between start and end by t."""
    return start + (end - start) * t


def random_choice(options):
    """Return a random choice from a list of options."""
    return random.choice(options)


def distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def is_colliding(rect1, rect2):
    """Check if two rectangles are colliding."""
    return (rect1[0] < rect2[0] + rect2[2] and
            rect1[0] + rect1[2] > rect2[0] and
            rect1[1] < rect2[1] + rect2[3] and
            rect1[1] + rect1[3] > rect2[1])


def normalize(vector):
    """Normalize a 2D vector."""
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if length == 0:
        return (0, 0)
    return (vector[0] / length, vector[1] / length)