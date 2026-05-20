import random
import math

def generate_random_point(x_range, y_range):
    """Generates a random point within given x and y range."""
    x = random.uniform(*x_range)
    y = random.uniform(*y_range)
    return (x, y)

def distance_between_points(point1, point2):
    """Calculates Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def clamp(value, min_value, max_value):
    """Clamps a value between min and max values."""
    return max(min_value, min(value, max_value))

def interpolate(start, end, t):
    """Linearly interpolates between two values based on t value (0.0 to 1.0)."""
    return start + (end - start) * t

def load_sprite(image_path):
    """Loads and returns a sprite image from a given path."""
    from PIL import Image
    return Image.open(image_path)

def save_sprite(sprite, save_path):
    """Saves a sprite image to a given path."""
    sprite.save(save_path)